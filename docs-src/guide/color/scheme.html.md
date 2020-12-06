<h1 style="text-align: center; border: 0; margin-top: 0;">Color System</h1>
<div style="text-align: center; font-size: 5rem;">
    <pkt-icon set="adwaita" name="preferences-color"></pkt-icon>
</div>

# Scheme and UI Class
Packet UI generates color scheme from primary color (analog, triadic, complement
and monochrome). The default primary color is <span class="pkt-tag">amber</span>

To use analog and triadic color
- Apply class `color-{p, a1, a2, c, t1, t2}` for font and icon color
- Apply class `bg-{p, a1, a2, c, t1, t2}` for background
- Apply class `bg-int-{p, a1, a2, c, t1, t2}` for interactive background color `(hover and active)`.

Analog and Triadic color:
<div class="flex">
    <pkt-tag class="bg-a1">alalog left</pkt-tag>
    <pkt-tag class="bg-p">primary</pkt-tag>
    <pkt-tag class="bg-a2">alalog right</pkt-tag>
    <pkt-tag class="bg-t1">triadic left</pkt-tag>
    <pkt-tag class="bg-c">complement</pkt-tag>
    <pkt-tag class="bg-t2">triadic right</pkt-tag>
</div>

```html
<pkt-tag class="bg-a1">alalog left</pkt-tag>
<pkt-tag class="bg-p">primary</pkt-tag>
<pkt-tag class="bg-a2">alalog right</pkt-tag>
<pkt-tag class="bg-t1">triadic left</pkt-tag>
<pkt-tag class="bg-c">complement</pkt-tag>
<pkt-tag class="bg-t2">triadic right</pkt-tag>
```

Interactive Background Color:
<div class="flex">
    <pkt-tag class="bg-int-red">red</pkt-tag>
    <pkt-tag class="bg-int-orange">orange</pkt-tag>
    <pkt-tag class="bg-int-yellow">yellow</pkt-tag>
    <pkt-tag class="bg-int-green">green</pkt-tag>
    <pkt-tag class="bg-int-blue">blue</pkt-tag>
    <pkt-tag class="bg-int-purple">purple</pkt-tag>
</div>

```html
<pkt-tag class="bg-int-red">red</pkt-tag>
<pkt-tag class="bg-int-orange">orange</pkt-tag>
<pkt-tag class="bg-int-yellow">yellow</pkt-tag>
<pkt-tag class="bg-int-green">green</pkt-tag>
<pkt-tag class="bg-int-blue">blue</pkt-tag>
<pkt-tag class="bg-int-purple">purple</pkt-tag>
```

Monochrome for primary color):
<div class="flex">
    <pkt-tag class="bg-p d4">darken 4</pkt-tag>
    <pkt-tag class="bg-p d3">darken 3</pkt-tag>
    <pkt-tag class="bg-p d2">darken 2</pkt-tag>
    <pkt-tag class="bg-p d1">darken 1</pkt-tag>
    <pkt-tag class="bg-p">primary</pkt-tag>
    <pkt-tag class="bg-p l1">lighten 1</pkt-tag>
    <pkt-tag class="bg-p l2">lighten 2</pkt-tag>
    <pkt-tag class="bg-p l3">lighten 3</pkt-tag>
    <pkt-tag class="bg-p l4">lighten 4</pkt-tag>
</div>

```html
<pkt-tag class="bg-p d4">darken 4</pkt-tag>
<pkt-tag class="bg-p d3">darken 3</pkt-tag>
<pkt-tag class="bg-p d2">darken 2</pkt-tag>
<pkt-tag class="bg-p d1">darken 1</pkt-tag>
<pkt-tag class="bg-p">primary</pkt-tag>
<pkt-tag class="bg-p l1">lighten 1</pkt-tag>
<pkt-tag class="bg-p l2">lighten 2</pkt-tag>
<pkt-tag class="bg-p l3">lighten 3</pkt-tag>
<pkt-tag class="bg-p l4">lighten 4</pkt-tag>
```

# Change Primary Color ?
The primary color can be changed by using `node_modules/packet-ui/src/style/_var.scss`.
See color customization for more details.
