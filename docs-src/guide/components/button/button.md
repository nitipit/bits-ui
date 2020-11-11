<h1 style="border: 0; margin: 0; text-align: center;">Button</h1>

# Preview
<div id="preview">
    <div class="flex">
        <button>Button</button>
        <span class="bits-button-pin">+</span>
        <span class="bits-button-square">
            <bits-icon theme="adwaita" name="emblem-shared"></bits-icon>
        </span>
    </div>
    <div class="flex">
        <div class="bits-button-group" style="width: 10rem;">
            <button class="bg-int-a1">OK</button>
            <button class="bg-int-white">Cancel</button>
        </div>
        <div class="bits-button-group" style="display: inline-flex;">
            <span class="bits-button-square bg-int-p">
                <bits-icon theme="adwaita" name="media-playback-start"></bits-icon>
            </span>
            <span class="bits-button-square bg-int-p">
                <bits-icon theme="adwaita" name="media-playback-stop"></bits-icon>
            </span>
            <span class="bits-button-square bg-int-c">
                <bits-icon theme="adwaita" name="media-skip-backward"></bits-icon>
            </span>
            <span class="bits-button-square bg-int-c">
                <bits-icon theme="adwaita" name="media-skip-forward"></bits-icon>
            </span>
        </div>
    </div>
    <div class="flex">
        <button class="bg-int-a2" style="font-size: 2rem">Big Button</button>
    </div>
</div>

# Usage
## Button
<button>Button</button>
```html
<button>button</button>
<a class="button">button</a>
```
## Pin
<span class="bits-button-pin">+</span>
```html
<bits-button-pin>+</bits-button-pin>
<a class="bits-button-pin">+</a>
```
## Square Button
<span class="bits-button-square">+</span>

```html
<bits-button-square>+</bits-button-square>
<a class="bits-button-square">+</a>
```

## Group Button
Grouping buttons together. Can apply on `button` and `bits-button-square`

<div class="flex p">
    <bits-button-group style="width: 10rem;">
        <button class="bg-int-a1">OK</button>
        <button class="bg-int-white">Cancel</button>
    </bits-button-group>
    <bits-button-group style="margin-left: 2rem;">
        <bits-button-square class="bg-int-p">
            <bits-icon theme="adwaita" name="media-playback-start"></bits-icon>
        </bits-button-square>
        <bits-button-square class="bg-int-p">
            <bits-icon theme="adwaita" name="media-playback-stop"></bits-icon>
        </bits-button-square>
        <bits-button-square class="bg-int-c">
            <bits-icon theme="adwaita" name="media-skip-backward"></bits-icon>
        </bits-button-square>
        <bits-button-square class="bg-int-c">
            <bits-icon theme="adwaita" name="media-skip-forward"></bits-icon>
        </bits-button-square>
    </bits-button-group>
</div>

```html
<bits-button-group>
    <button class="bg-int-a1">OK</button>
    <button class="bg-int-white">Cancel</button>
</bits-button-group>
<bits-button-group>
    <bits-button-square class="bg-int-p">
        <bits-icon theme="adwaita" name="media-playback-start"></bits-icon>
    </bits-button-square>
    <bits-button-square class="bg-int-p">
        <bits-icon theme="adwaita" name="media-playback-stop"></bits-icon>
    </bits-button-square>
    <bits-button-square class="bg-int-c">
        <bits-icon theme="adwaita" name="media-skip-backward"></bits-icon>
    </bits-button-square>
    <bits-button-square class="bg-int-c">
        <bits-icon theme="adwaita" name="media-skip-forward"></bits-icon>
    </bits-button-square>
</bits-button-group>
```

# Stylus

<div>
    <bits-tag>button</bits-tag>
</div>

```stylus
button(
    $bg-color: $ui-color,
    $radius: $border-radius)
```

|Argument|Description|Example value|
|---|---|---|
|`$bg-color`|Background color|`red` `$color-p`|
|`$radius`|Button border radius|`4px`|

<div style="margin-top: 2rem;">
    <bits-tag>button-pin</bits-tag>
</div>

```stylus
button-pin($bg-color: $ui-color)
```

|Argument|Description|Example value|
|---|---|---|
|`$bg-color`|Background color|`red` `$color-p`|

<div style="margin-top: 2rem;">
    <bits-tag>button-square</bits-tag>
</div>

```stylus
button-square($bg-color: $ui-color)
```

|Argument|Description|Example value|
|---|---|---|
|`$bg-color`|Background color|`red` `$color-p`|

<div style="margin-top: 2rem;">
    <bits-tag>button-group</bits-tag>
</div>

```stylus
button-gruop($radius: $border-radius)
```

|Argument|Description|Example value|
|---|---|---|
|`$radius`|Button border radius|`4px`|
