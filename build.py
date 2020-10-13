import asyncio
from pathlib import Path
import shutil


base_dir = Path(__file__).parent


async def packet_ui():
    proc = await asyncio.create_subprocess_shell(
        'yarn run parcel build src/packet-ui.js')
    await proc.communicate()

    proc = await asyncio.create_subprocess_shell(
        'yarn run sass src/:dist/')
    await proc.communicate()

    src_dir = base_dir.joinpath('src/style')
    dest_dir = base_dir.joinpath('dist/style')
    shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)

    src_dir = base_dir.joinpath('src/ui')
    dest_dir = base_dir.joinpath('dist/ui')
    shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)


async def lib():
    proc = await asyncio.create_subprocess_shell(
        'yarn run parcel build node_modules/normalize.css/normalize.css')
    await proc.communicate()


async def font():
    shutil.copytree(
        base_dir.joinpath('src/font'),
        base_dir.joinpath('dist/font'),
        dirs_exist_ok=True,
    )


async def main():
    await packet_ui()
    await lib()
    await font()

asyncio.run(main())
