# Pallete

<div id="pallete" style="margin: 2rem 0;">
    <div class="row">
        <div class="bg-int-red"></div>
        <div class="bg-int-pink"></div>
        <div class="bg-int-purple"></div>
        <div class="bg-int-deep-purple"></div>
    </div>
    <div class="row">
        <div class="bg-int-indigo"></div>
        <div class="bg-int-blue"></div>
        <div class="bg-int-light-blue"></div>
        <div class="bg-int-cyan"></div>
    </div>
    <div class="row">
        <div class="bg-int-teal"></div>
        <div class="bg-int-green"></div>
        <div class="bg-int-light-green"></div>
        <div class="bg-int-lime"></div>
    </div>
    <div class="row">
        <div class="bg-int-yellow"></div>
        <div class="bg-int-amber"></div>
        <div class="bg-int-orange"></div>
        <div class="bg-int-deep-orange"></div>
    </div>
    <div class="row">
        <div class="bg-int-brown"></div>
        <div class="bg-int-grey"></div>
        <div class="bg-int-blue-grey"></div>
        <div class="bg-int-black"></div>
    </div>
</div>

Packet UI provides 19 predefined color pallete from Material Design.

<div id="badge">
    <pkt-badge class="bg-red">red</pkt-badge>
    <pkt-badge class="bg-pink">pink</pkt-badge>
    <pkt-badge class="bg-purple">purple</pkt-badge>
    <pkt-badge class="bg-deep-purple">deep-purple</pkt-badge>
    <pkt-badge class="bg-indigo">indigo</pkt-badge>
    <pkt-badge class="bg-blue">blue</pkt-badge>
    <pkt-badge class="bg-light-blue">light-blue</pkt-badge>
    <pkt-badge class="bg-cyan">cyan</pkt-badge>
    <pkt-badge class="bg-teal">teal</pkt-badge>
    <pkt-badge class="bg-green">green</pkt-badge>
    <pkt-badge class="bg-light-green">light-green</pkt-badge>
    <pkt-badge class="bg-lime">lime</pkt-badge>
    <pkt-badge class="bg-yellow">yellow</pkt-badge>
    <pkt-badge class="bg-amber">amber</pkt-badge>
    <pkt-badge class="bg-orange">orange</pkt-badge>
    <pkt-badge class="bg-deep-orange">deep-orange</pkt-badge>
    <pkt-badge class="bg-brown">brown</pkt-badge>
    <pkt-badge class="bg-grey">grey</pkt-badge>
    <pkt-badge class="bg-blue-grey">blue-grey</pkt-badge>
</div>

To use color pallete, just apply predefined css class following.
- `class="{color}"` for text color.
- `class="{bg-color}"` for background color.
- `class="{bg-int-color}"` for interactive background color.

For example:

<span class="indigo">indigo</span>
<pkt-tag class="bg-red">bg-red</pkt-tag>
<pkt-tag class="bg-int-purple">bg-int-purple</pkt-tag>

```html
<span class="indigo">indigo</span>
<pkt-tag class="bg-red">bg-red</pkt-tag>
<pkt-tag class="bg-int-purple">bg-int-purple</pkt-tag>
```

> text color will change between black/white depends on background color.
