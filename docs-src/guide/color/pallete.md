<h1 style="text-align: center; border: 0; margin-top: 0;">Color System</h1>
<div style="text-align: center; font-size: 5rem;">
    <icon theme="adwaita" name="preferences-color"></icon>
</div>

# Pallete

<div id="pallete" style="margin: 2rem 0;">
    <div class="bits-button-group">
        <button class="bg-red"></button>
        <button class="bg-pink"></button>
        <button class="bg-purple"></button>
        <button class="bg-deep-purple"></button>
    </div>
    <div class="bits-button-group">
        <button class="bg-indigo"></button>
        <button class="bg-blue"></button>
        <button class="bg-light-blue"></button>
        <button class="bg-cyan"></button>
    </div>
    <div class="bits-button-group">
        <button class="bg-teal"></button>
        <button class="bg-green"></button>
        <button class="bg-light-green"></button>
        <button class="bg-lime"></button>
    </div>
    <div class="bits-button-group">
        <button class="bg-yellow"></button>
        <button class="bg-amber"></button>
        <button class="bg-orange"></button>
        <button class="bg-deep-orange"></button>
    </div>
    <div class="bits-button-group">
        <button class="bg-brown"></button>
        <button class="bg-grey"></button>
        <button class="bg-blue-grey"></button>
        <button class="bg-black"></button>
    </div>
</div>

Bits UI has 19 predefined color pallete from Material Design.

> red, pink, purple, deep-purple, indigo, blue, light-blue, cyan, teal, green, light-green, lime, yellow, amber, orange, deep-orange, brown, grey, blue-grey

To use color pallet, just apply `class="{color}"` for text color and `class="bg-{color}"` for background color.
For example:

<tag class="bg-indigo">Hello</tag>
<span class="indigo">I'm Indigo</span>

```html
<tag class="bg-indigo">Hello</tag>
<!-- bg-indigo is dark shade. Text color will become white. -->
<span class="indigo">I'm indigo</span>
```

> `class="bg-{color}"` also apply css white/black font color depends on background's hue and lightness for readability.
