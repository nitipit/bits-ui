import asyncio
import shutil
from pathlib import Path
from watchgod import awatch, Change


_dir = Path(__file__).parent
_docs_dir = _dir.joinpath('docs')
_dist_dir = _dir.joinpath('dist')


def lib():
    shutil.copytree(
        _dir.joinpath('node_modules/adwaita-icon-web/dist/'),
        'docs/static/lib/adwaita-icon-web/',
        dirs_exist_ok=True)
    shutil.copytree(
        _dir.joinpath('node_modules/highlight.js/styles/'),
        'docs/static/lib/highlight.js/',
        dirs_exist_ok=True)


async def engrave():
    proc = await asyncio.create_subprocess_shell('engrave dev docs-src docs')
    await proc.communicate()
    proc.terminate()


async def packet_ui():
    dest_dir = _docs_dir.joinpath('static/lib/packet-ui')
    shutil.copytree(_dist_dir, dest_dir, dirs_exist_ok=True)
    async for changes in awatch(_dir.joinpath('dist/')):
        for change, path in changes:
            dest = Path(path).relative_to(_dist_dir)
            dest = dest_dir.joinpath(dest)
            if change == Change.deleted:
                dest.unlink()
                print(f'{str(change)} : {dest}')
            if (change == Change.added) or (change == Change.modified):
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(path, dest)
                print(f'{str(change)} : {dest.relative_to(_docs_dir)}')


async def main():
    lib()
    await asyncio.gather(
        engrave(),
        packet_ui(),
    )


asyncio.run(main())
