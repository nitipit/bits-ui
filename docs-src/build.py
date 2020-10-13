from pathlib import Path
from datetime import datetime
import asyncio
import shutil
import argparse
import re
from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import contextfunction
import mistune
from watchgod import awatch, Change


base_dir = Path(__file__).resolve().parent
docs_dir = base_dir.parent.joinpath('docs')


class HTML:
    def __init__(
            self,
            mode='build',
            template_dir=base_dir.joinpath('template'),
            asset_dir=base_dir.joinpath('asset')):
        @contextfunction
        def markdown(context, path):
            path = template_dir\
                .joinpath(Path(context.name)).parent\
                .joinpath(path)
            html = mistune.html(open(path).read())
            return html

        template = Environment(
            loader=FileSystemLoader(base_dir.joinpath('template')),
            trim_blocks=True,
        )
        template.globals['datetime'] = datetime
        template.globals['markdown'] = markdown
        template = template.get_template

        self.mode = mode
        self.template_dir = template_dir
        self.template = template
        self.asset_dir = asset_dir

    def _template_to_html(self, template_path):
        template_path = Path(template_path).relative_to(self.template_dir)
        html = self.template(str(template_path)).render()
        html_path = docs_dir.joinpath(template_path)
        html_path.parent.mkdir(parents=True, exist_ok=True)
        f = open(html_path, 'w')
        f.write(html)
        f.close()
        print(f'Render template: {template_path}')

    def _template_dir_build(
            self, dir_path=None, traverse=True):
        if dir_path is None:
            dir_path = self.template_dir
        if traverse is True:
            glob = dir_path.glob('**/*')
        else:
            glob = dir_path.glob('*')
        for path in glob:
            if re.match('^_.*.html$', path.name):
                continue
            if path.suffix == '.html':
                self._template_to_html(path)
                continue
            if re.match('(.jpg|.png)', path.suffix):
                self._static_file_copy(path)

    def _static_file_copy(self, path: Path):
        path = Path(path)
        relative_path = path.relative_to(self.template_dir)
        dest = docs_dir.joinpath(relative_path)
        shutil.copy(path, dest)
        print(f"Static file: {relative_path}")

    async def build_template(self):
        self._template_dir_build()
        async for changes in awatch(self.template_dir):
            for change, path in changes:
                path = Path(path)
                if change == Change.deleted:
                    continue
                if re.match('^_.*.html$', path.name):
                    # Build all html files in all traversed directories.
                    self._template_dir_build(
                        dir_path=path.parent, traverse=True)
                    continue
                if path.suffix == '.html':
                    self._template_to_html(path)
                if path.suffix == '.md':
                    # Build all html files in current directory.
                    self._template_dir_build(
                        dir_path=path.parent, traverse=False)
                if re.match('(.jpg|.png)', path.suffix):
                    self._static_file_copy(path)

    async def build_css(self):
        await asyncio.create_subprocess_shell(
            f'yarn run sass --watch {self.template_dir}:docs/')

    async def build_js(self):
        for js_path in self.template_dir.glob('**/*.js'):
            if self.mode == 'build':
                await asyncio.create_subprocess_shell(
                    f"yarn parcel build {js_path} " +
                    f"--dist-dir {docs_dir}")
            elif self.mode == 'dev':
                await asyncio.create_subprocess_shell(
                    f"yarn parcel watch {js_path} " +
                    f"--dist-dir {docs_dir}")

    async def build_asset(self):
        shutil.copytree(
            base_dir.joinpath('asset'),
            docs_dir.joinpath('static', 'asset'),
            dirs_exist_ok=True)

        print('build asset')

        async for changes in awatch(f"{self.asset_dir}"):
            for change, path in changes:
                if change == Change.deleted:
                    continue
                path = Path(path)
                asset_relative_path = path.relative_to(self.asset_dir)
                dest = docs_dir.joinpath(
                    'static', 'asset', asset_relative_path)
                shutil.copy(path, dest)

            print(f"asset: {asset_relative_path}")

    async def tasks(self):
        return await asyncio.gather(
            self.build_template(),
            self.build_css(),
            self.build_asset(),
            self.build_js(),
        )


async def lib():
    shutil.copytree(
        base_dir.parent.joinpath('dist'),
        docs_dir.joinpath('static', 'lib', 'packet-ui'),
        dirs_exist_ok=True)


async def node_modules():
    node_modules_dir = base_dir.parent.joinpath('node_modules')

    src = node_modules_dir.joinpath('adwaita-icon-web', 'dist', 'adwaita.svg')
    dest = docs_dir.joinpath(
        'static/lib/adwaita-icon-web/')
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copy(src, dest)

    src = node_modules_dir.joinpath('highlight.js/styles/atom-one-dark.css')
    dest_dir = docs_dir.joinpath(
        'static/lib/highlight.js/styles/'
    )
    dest_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(src, dest_dir)


async def server():
    await asyncio.create_subprocess_shell(
        "python -m http.server 8000 --bind 0.0.0.0 " +
        f"--directory {docs_dir}")


async def main():
    parser = argparse.ArgumentParser(description='docs builder')
    parser.add_argument(
        'mode', default='build', nargs='?',
        help="'build' or 'dev'")

    args = parser.parse_args()

    await asyncio.gather(
        HTML(mode=args.mode).tasks(),
        lib(),
        node_modules(),
        server(),
    )

asyncio.run(main())
