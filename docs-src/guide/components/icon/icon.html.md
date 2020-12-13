# Icon

## Preview
---
<div id="preview">
    <pkt-icon class="size-1 red" set="adwaita" name="airplane-mode"></pkt-icon>
    <pkt-icon class="size-2 purple" set="adwaita" name="call-start"></pkt-icon>
    <pkt-icon class="size-3" set="adwaita" name="contact-new"></pkt-icon>
    <pkt-icon class="size-2 blue" set="adwaita" name="find-location"></pkt-icon>
    <pkt-icon class="size-1 green" set="adwaita" name="go-home"></pkt-icon>
</div>

Packet UI provides icon set from [adwaita-icon-web](https://nitipit.github.io/adwaita-icon-web/).

## Usage
---

Before using, we need to load **adwaita.svg** in `<head>` section.

> <pkt-icon set="adwaita" name="dialog-information"></pkt-icon> `adwaita.svg` is included in Packet UI distribution.


```html
<head>
<link icon
    rel="preload"
    set="adwaita"
    href="/path/to/packet-ui/adwaita-icon-web/adwaita.svg"
    as="image" type="image/svg+xml">
</head>
```

Then we can use `<pkt-icon>` by specify icon set and icon name.
Furthermore, color and size can be applied by using css property: `color` & `font-size` as following example.


```html
<pkt-icon set="adwaita" name="airplane-mode"></pkt-icon>

<!-- with color and size -->
<pkt-icon set="adwaita" name="airplane-mode"
    style="color: red; font-size: 2em;">
</pkt-icon>

<!-- using predefined color CSS class -->
<pkt-icon set="adwaita" name="airplane-mode"
    class="red"
</pkt-icon>
```