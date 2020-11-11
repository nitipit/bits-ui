<h1 style="text-align: center; border: 0; margin-top: 0;">Color System</h1>
<div style="text-align: center; font-size: 5rem;">
    <bits-icon theme="adwaita" name="preferences-color"></bits-icon>
</div>

# Scheme and UI Class
Bits UI generates color scheme from primary color (analog, triadic, complement
and monochrome). The default primary color is <span class="bits-tag">amber</span>

To use analog and triadic color
- Apply class `color-{p, a1, a2, c, t1, t2}` for font and icon color
- Apply class `bg-{p, a1, a2, c, t1, t2}` for background
- Apply class `bg-int-{p, a1, a2, c, t1, t2}` for interactive background color `(hover and active)`.

Analog and Triadic color:
<div class="flex">
    <bits-tag class="bg-a1">alalog left</bits-tag>
    <bits-tag class="bg-p">primary</bits-tag>
    <bits-tag class="bg-a2">alalog right</bits-tag>
    <bits-tag class="bg-t1">triadic left</bits-tag>
    <bits-tag class="bg-c">complement</bits-tag>
    <bits-tag class="bg-t2">triadic right</bits-tag>
</div>

```html
<bits-tag class="bg-a1">alalog left</bits-tag>
<bits-tag class="bg-p">primary</bits-tag>
<bits-tag class="bg-a2">alalog right</bits-tag>
<bits-tag class="bg-t1">triadic left</bits-tag>
<bits-tag class="bg-c">complement</bits-tag>
<bits-tag class="bg-t2">triadic right</bits-tag>
```

Interactive Background Color:
<div class="flex">
    <bits-tag class="bg-int-red">red</bits-tag>
    <bits-tag class="bg-int-orange">orange</bits-tag>
    <bits-tag class="bg-int-yellow">yellow</bits-tag>
    <bits-tag class="bg-int-green">green</bits-tag>
    <bits-tag class="bg-int-blue">blue</bits-tag>
    <bits-tag class="bg-int-purple">purple</bits-tag>
</div>

```html
<bits-tag class="bg-int-red">red</bits-tag>
<bits-tag class="bg-int-orange">orange</bits-tag>
<bits-tag class="bg-int-yellow">yellow</bits-tag>
<bits-tag class="bg-int-green">green</bits-tag>
<bits-tag class="bg-int-blue">blue</bits-tag>
<bits-tag class="bg-int-purple">purple</bits-tag>
```

Monochrome for primary color):
<div class="flex">
    <bits-tag class="bg-p d4">darken 4</bits-tag>
    <bits-tag class="bg-p d3">darken 3</bits-tag>
    <bits-tag class="bg-p d2">darken 2</bits-tag>
    <bits-tag class="bg-p d1">darken 1</bits-tag>
    <bits-tag class="bg-p">primary</bits-tag>
    <bits-tag class="bg-p l1">lighten 1</bits-tag>
    <bits-tag class="bg-p l2">lighten 2</bits-tag>
    <bits-tag class="bg-p l3">lighten 3</bits-tag>
    <bits-tag class="bg-p l4">lighten 4</bits-tag>
</div>

```html
<bits-tag class="bg-p d4">darken 4</bits-tag>
<bits-tag class="bg-p d3">darken 3</bits-tag>
<bits-tag class="bg-p d2">darken 2</bits-tag>
<bits-tag class="bg-p d1">darken 1</bits-tag>
<bits-tag class="bg-p">primary</bits-tag>
<bits-tag class="bg-p l1">lighten 1</bits-tag>
<bits-tag class="bg-p l2">lighten 2</bits-tag>
<bits-tag class="bg-p l3">lighten 3</bits-tag>
<bits-tag class="bg-p l4">lighten 4</bits-tag>
```

# Change Primary Color ?
The primary color can be changed by using `node_modules/bits-ui/src/stylus/_var.styl`.
See color customization for more details.
