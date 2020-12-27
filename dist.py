import asyncio
from pathlib import Path
import shutil
import argparse
from watchgod import awatch, Change


class PacketUI:
    def __init__(
            self, src_dir: Path,
            dist_dir: Path,
            node_modules_dir: Path):
        self.src_dir = src_dir.resolve()
        self.dist_dir = dist_dir.resolve()
        self.node_modules_dir = node_modules_dir

    async def _scss(self):
        proc = await asyncio.create_subprocess_shell(
            f"npx sass {self.src_dir}:{self.dist_dir}"
        )
        await proc.communicate()

    async def _src_copy(self):
        # Copy SCSS
        src_dir = self.src_dir.joinpath('style')
        dest_dir = self.dist_dir.joinpath('style')
        shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)

        # Copy UI JS & SCSS
        src_dir = self.src_dir.joinpath('ui')
        dest_dir = self.dist_dir.joinpath('ui')
        shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)
        proc = await asyncio.create_subprocess_shell(
            f"npx parcel build --dist-dir {self.dist_dir} "
            f"{self.node_modules_dir.joinpath('normalize.css/normalize.css')}"
        )
        await proc.communicate()

        # Copy Fonts
        shutil.copytree(
            self.src_dir.joinpath('font'),
            self.dist_dir.joinpath('font'),
            dirs_exist_ok=True,
        )

    async def build(self):
        # Build packet-ui.js
        proc = await asyncio.create_subprocess_shell(
            f"npx parcel build --dist-dir {self.dist_dir} "
            f"{self.src_dir.joinpath('packet-ui.js')}"
        )
        await proc.communicate()

        # Build SCSS
        proc = await asyncio.create_subprocess_shell(
            f"npx sass {self.src_dir}:{self.dist_dir}"
        )
        await proc.communicate()

        # Copy source files
        await self._src_copy()

    async def _parcel_watch(self):
        proc = await asyncio.create_subprocess_shell(
            f"npx parcel watch --dist-dir {self.dist_dir} "
            f"{self.src_dir.joinpath('packet-ui.js')}")
        await proc.communicate()
        proc.terminate()

    async def _sass_watch(self):
        proc = await asyncio.create_subprocess_shell(
            f"npx sass --watch {self.src_dir}:{self.dist_dir}"
        )
        await proc.communicate()
        proc.terminate()

    async def _file_watch(self):
        async for changes in awatch(self.src_dir):
            for change, path in changes:
                path = Path(path)
                dest = path.relative_to(self.src_dir)
                dest = self.dist_dir.joinpath(dest)
                if (path.suffix == '.js')\
                        or (path.suffix == '.scss')\
                        or (path.suffix == '.sass'):
                    pass
                if change == Change.deleted:
                    dest.unlink()
                else:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy(path, dest)
                    print(f'copied: {dest}')

    async def dev(self):
        await asyncio.gather(
            self._parcel_watch(),
            self._sass_watch(),
            self._file_watch(),
        )


def lib(base_dir: Path):
    src_dir = base_dir.joinpath('node_modules/adwaita-icon-web/dist/')
    dest_dir = base_dir.joinpath('dist/adwaita-icon-web/')
    dest_dir.mkdir(parents=True, exist_ok=True)
    shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)


async def main():
    base_dir = Path(__file__).parent
    lib(base_dir)
    packet_ui = PacketUI(
        src_dir=base_dir.joinpath('src'),
        dist_dir=base_dir.joinpath('dist'),
        node_modules_dir=base_dir.joinpath('node_modules')
    )

    parser = argparse.ArgumentParser(description='Packet UI Distribution')
    parser.add_argument('mode', nargs='?', default='build')

    args = parser.parse_args()
    if args.mode == 'dev':
        await packet_ui.dev()
    else:
        await packet_ui.build()


asyncio.run(main())
