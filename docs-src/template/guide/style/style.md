<h1 style="margin:0; border: 0; text-align: center;">Stylus Mixins</h1>

Using stylus function/mixin is the recommend way to change or customize tag style.
Just use `@require 'node_modules/bits-ui/src/stylus/_require'` then all variables and functions will be ready to use.

Let's see stylus function/mixin for <tag>box-arrow</tag>

```stylus
@require 'node_modules/bits-ui/src/stylus/_require'

// Stylus function for bits-box-arrow-top
bits-box-arrow-top
    box-arrow(
        $arrow=top,
        $arrow-size=7px,
        $bg-color=lighten(grey, 80%),
        $border-width=1px,
        $border-color=black,
        $radius=$border-radius)
```

For example, to customize `bits-box-arrow-top` css
to change arrow size and background color.

```stylus
// file: box-arrow.styl
@require 'node_modules/bits-ui/src/stylus/_require'

bits-box-arrow-top
    box-arrow(
        $arrow-size: 1em,
        $bg-color: $color-p)
```
Compile stylus to CSS, then load use it in web page.
```bash
$ stylus box-arrow.styl
```

```html
<!-- <head> -->
<link rel="stylesheet" href="box-arrow.css">

<!-- <body> -->
<bits-box-arrow-top>
    Lorem Ipsum is simply dummy text of the printing and typesetting industry.
    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
    when an unknown printer took a galley of type and scrambled it
    to make a type specimen book. It has survived not only five centuries,
    but also the leap into electronic typesetting, remaining essentially unchanged.
</bits-box-arrow-top>
```

<div class="p" style="margin-top: 2rem;">
    <bits-box-arrow-top>
        Lorem Ipsum is simply dummy text of the printing and typesetting industry.
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
        when an unknown printer took a galley of type and scrambled it
        to make a type specimen book. It has survived not only five centuries,
        but also the leap into electronic typesetting, remaining essentially unchanged.
    </bits-box-arrow-top>
</div>
