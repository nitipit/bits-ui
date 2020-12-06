<h1 style="text-align: center; border: 0; margin-top: 0;">Color System</h1>
<div style="text-align: center; font-size: 5rem;">
    <pkt-icon set="adwaita" name="preferences-color"></pkt-icon>
</div>

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

Bits UI has 19 predefined color pallete from Material Design.

> red, pink, purple, deep-purple, indigo, blue, light-blue, cyan, teal, green, light-green, lime, yellow, amber, orange, deep-orange, brown, grey, blue-grey

To use color pallet, just apply `class="{color}"` for text color and `class="bg-int-{color}"` for background color.
For example:

<tag class="bg-int-indigo">Hello</tag>
<span class="indigo">I'm Indigo</span>

```html
<tag class="bg-int-indigo">Hello</tag>
<!-- bg-int-indigo is dark shade. Text color will become white. -->
<span class="indigo">I'm indigo</span>
```

> `class="bg-int-{color}"` also apply css white/black font color depends on background's hue and lightness for readability.
