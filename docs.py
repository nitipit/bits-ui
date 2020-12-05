import asyncio
import shutil
from pathlib import Path


_dir = Path(__file__).parent


def lib():
    shutil.copytree(
        _dir.joinpath('dist/'), 'docs/static/lib/packet-ui/',
        dirs_exist_ok=True)
    shutil.copytree(
        _dir.joinpath('node_modules/adwaita-icon-web/dist/'),
        'docs/static/lib/adwaita-icon-web/',
        dirs_exist_ok=True)
    shutil.copytree(
        _dir.joinpath('node_modules/highlight.js/styles/'),
        'docs/static/lib/highlight.js/',
        dirs_exist_ok=True)


async def main():
    lib()
    proc = await asyncio.create_subprocess_shell('pillari dev docs-src docs')
    await proc.communicate()
    proc.terminate()


asyncio.run(main())
