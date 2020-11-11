import asyncio
from pathlib import Path
import shutil
import argparse


class Docs:
    def __init__(self, base_dir: Path, src_dir: Path, docs_dir: Path):
        self.base_dir = base_dir.resolve()
        self.src_dir = src_dir.resolve()
        self.docs_dir = docs_dir.resolve()

    def _copy_lib(self):
        # Copy packet-ui
        shutil.copytree(
            self.base_dir.joinpath('dist'),
            self.docs_dir.joinpath('static/lib/packet-ui/'),
            dirs_exist_ok=True,
        )

        # Copy adwaita-icon-web
        shutil.copytree(
            self.base_dir.joinpath('node_modules/adwaita-icon-web/dist'),
            self.docs_dir.joinpath('static/lib/adwaita-icon-web'),
            dirs_exist_ok=True,
        )

        # Copy highlight.js
        shutil.copytree(
            self.base_dir.joinpath('node_modules/highlight.js'),
            self.docs_dir.joinpath('static/lib/highlight.js'),
            dirs_exist_ok=True,
        )

    async def build(self):
        self._copy_lib()
        proc = await asyncio.create_subprocess_shell(
            f"pillari {self.src_dir} {self.docs_dir}"
        )
        await proc.communicate()

    async def dev(self):
        self._copy_lib()
        proc = await asyncio.create_subprocess_shell(
            f"pillari --dev {self.src_dir} {self.docs_dir}"
        )
        await proc.communicate()


async def main():
    base_dir = Path(__file__).parent
    docs = Docs(
        base_dir=base_dir,
        src_dir=base_dir.joinpath('docs-src'),
        docs_dir=base_dir.joinpath('docs')
    )
    arg_parser = argparse.ArgumentParser(description="Packet UI Documentation")
    arg_parser.add_argument('--dev', action='store_true')
    arg_parser.add_argument(
        'src', nargs='?', default="docs-src", help="source directory")
    arg_parser.add_argument(
        'dest', nargs='?', default='docs', help="destination directory")
    args = arg_parser.parse_args()
    if args.dev is True:
        await docs.dev()
    else:
        await docs.build()


asyncio.run(main())
