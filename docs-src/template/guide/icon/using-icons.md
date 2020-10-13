<h1 style="margin: 0 auto 1rem 0; border: 0; text-align: center;">Icon Systems</h1>
<div style="display: flex; justify-content: center; align-items: center;">
    <bits-icon theme="adwaita" name="view-app-grid" style="font-size: 8rem;"></bits-icon>
</div>

<h1 style="margin-top: 2rem;">Using Icons</h1>

Bits UI ships with Adwaita Symbolic SVG Icon. To use icons, `<link rel="svg-icon">` must be put in `<head>` section.

<hl data-line="2"></hl>
```html
<!-- in <head></head> section -->
<link rel="icon-svg" theme="adwaita" href="https://cdn.jsdelivr.net/npm/bits-ui@2.0.0/dist/icon/adwaita.svg">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bits-ui@2.0.0/dist/normalize.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bits-ui@2.0.0/dist/bits-ui.min.css">
<script src="https://cdn.jsdelivr.net/npm/bits-ui@2.0.0/dist/riot.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bits-ui@2.0.0/dist/bits-ui.js"></script>
```

Then use `<bits-icon>` in `<body>` section.

```html
<!-- In <body></body> section -->
<bits-icon theme="adwaita" name="airplane-mode"></bits-icon>
<bits-icon theme="adwaita" name="battery"></bits-icon>
<bits-icon theme="adwaita" name="emblem-shared"></bits-icon>
<bits-icon theme="adwaita" name="help-browser"></bits-icon>
```

<div id="icon-sample">
    <bits-icon theme="adwaita" name="airplane-mode"></bits-icon>
    <bits-icon theme="adwaita" name="battery"></bits-icon>
    <bits-icon theme="adwaita" name="emblem-shared"></bits-icon>
    <bits-icon theme="adwaita" name="help-browser"></bits-icon>
</div>

# Icon Style
Icon color and size can be easily change by CSS `color` and `font-size`

Bits UI Color palette a can also be applied by `class={color}`.

Example:
```html
<bits-icon theme="adwaita" name="airplane-mode" style="color: blue; font-size: 4rem;"></bits-icon>
<bits-icon theme="adwaita" class="blue" name="airplane-mode" style="font-size: 4rem;"></bits-icon>
```
<div style="display: flex; justify-content: center;">
    <bits-icon theme="adwaita" name="airplane-mode" style="color: blue; font-size: 4rem; margin: 0.5rem;"></bits-icon>
    <bits-icon theme="adwaita" class="blue" name="airplane-mode" style="font-size: 4rem; margin: 0.5rem;"></bits-icon>
</div>
