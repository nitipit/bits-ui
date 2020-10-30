<h1 style="margin: 0 auto 1rem 0; border: 0; text-align: center;">Theming</h1>

# How it works

Bits-UI theme is built with <span class="bits-tag bg-c">Stylus</span>.
Stylus code for theming is in `src/stylus/`


```bash
src
└── stylus
    ├── _media-query.styl
    ├── _mixin.styl
    ├── _require.styl
    ├── _typography.styl
    ├── _ui.styl
    ├── _var.styl # theme variables
    ├── bits-ui.styl # main stylus building file
    ├── default.styl # default
    ├── typography.styl # style for text and paragraph
    └── ui-class.styl
```

Let's say you have installed bits-ui, stylus files will be in
`node_modules/bits-ui/src/stylus/`. To build custom `bits-ui.css`, just
edit the file you want and run command

```bash
$ stylus node_modules/bits-ui/src/stylus/bits-ui.styl -o ./
```