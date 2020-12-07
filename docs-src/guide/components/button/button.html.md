# Button

## Preview
---
<div id="preview">
    <div class="flex">
        <button>Button</button>
        <span class="pkt-button-pin">+</span>
        <span class="pkt-button-square">
            <pkt-icon set="adwaita" name="emblem-shared"></pkt-icon>
        </span>
    </div>
    <div class="flex">
        <div class="pkt-button-group" style="width: 10rem;">
            <button class="bg-int-a1">OK</button>
            <button class="bg-int-white">Cancel</button>
        </div>
        <div class="pkt-button-group" style="display: inline-flex;">
            <span class="pkt-button-square bg-int-p">
                <pkt-icon set="adwaita" name="media-playback-start"></pkt-icon>
            </span>
            <span class="pkt-button-square bg-int-p">
                <pkt-icon set="adwaita" name="media-playback-stop"></pkt-icon>
            </span>
            <span class="pkt-button-square bg-int-c">
                <pkt-icon set="adwaita" name="media-skip-backward"></pkt-icon>
            </span>
            <span class="pkt-button-square bg-int-c">
                <pkt-icon set="adwaita" name="media-skip-forward"></pkt-icon>
            </span>
        </div>
    </div>
    <div class="flex">
        <button class="bg-int-a2" style="font-size: 2rem">Big Button</button>
    </div>
</div>

## Usage
---

### Button
<button>Button</button>
```html
<button>button</button>
<a class="button">button</a>
```
### Pin
<span class="pkt-button-pin">+</span>
```html
<pkt-button-pin>+</pkt-button-pin>
<a class="pkt-button-pin">+</a>
```
### Square Button
<span class="pkt-button-square">+</span>

```html
<pkt-button-square>+</pkt-button-square>
<a class="pkt-button-square">+</a>
```

### Group Button
Grouping buttons together. Can apply on `button` and `pkt-button-square`

<div class="flex p">
    <pkt-button-group style="width: 10rem;">
        <button class="bg-int-a1">OK</button>
        <button class="bg-int-white">Cancel</button>
    </pkt-button-group>
    <pkt-button-group style="margin-left: 2rem;">
        <pkt-button-square class="bg-int-p">
            <pkt-icon set="adwaita" name="media-playback-start"></pkt-icon>
        </pkt-button-square>
        <pkt-button-square class="bg-int-p">
            <pkt-icon set="adwaita" name="media-playback-stop"></pkt-icon>
        </pkt-button-square>
        <pkt-button-square class="bg-int-c">
            <pkt-icon set="adwaita" name="media-skip-backward"></pkt-icon>
        </pkt-button-square>
        <pkt-button-square class="bg-int-c">
            <pkt-icon set="adwaita" name="media-skip-forward"></pkt-icon>
        </pkt-button-square>
    </pkt-button-group>
</div>

```html
<pkt-button-group>
    <button class="bg-int-a1">OK</button>
    <button class="bg-int-white">Cancel</button>
</pkt-button-group>
<pkt-button-group>
    <pkt-button-square class="bg-int-p">
        <pkt-icon set="adwaita" name="media-playback-start"></pkt-icon>
    </pkt-button-square>
    <pkt-button-square class="bg-int-p">
        <pkt-icon set="adwaita" name="media-playback-stop"></pkt-icon>
    </pkt-button-square>
    <pkt-button-square class="bg-int-c">
        <pkt-icon set="adwaita" name="media-skip-backward"></pkt-icon>
    </pkt-button-square>
    <pkt-button-square class="bg-int-c">
        <pkt-icon set="adwaita" name="media-skip-forward"></pkt-icon>
    </pkt-button-square>
</pkt-button-group>
```

## SCSS
---
<div>
    Button<button style="margin-left: 1rem;">button</button>
</div>

```scss
@use 'path/to/_ui.scss';
@include ui.button(
    $bg-color: orange,
    $radius: 4px)
```

|Argument|Description|Example value|
|---|---|---|
|`$bg-color`|Background color|`red`|
|`$radius`|Border radius|`4px`|

<div style="margin-top: 2rem;">
    Button Pin<pkt-button-pin style="margin-left: 1rem;">+</pkt-button-pin>
</div>

```scss
@use 'path/to/_ui.scss';
@include button-pin($bg-color: $ui-color)
```

|Argument|Description|Example value|
|---|---|---|
|`$bg-color`|Background color|`red`|

<div style="margin-top: 2rem;">
    Square Button<pkt-button-square style="margin-left: 1rem;">+</pkt-button-square>
</div>

```scss
@use 'path/to/_ui.scss';
@include button-square($bg-color: $ui-color)
```

|Argument|Description|Example value|
|---|---|---|
|`$bg-color`|Background color|`red`|

<div style="margin-top: 2rem;">
    Group Button
    <div class="pkt-button-group" style="display: inline-flex; width: 8rem; margin-left: 1rem;">
        <button class="bg-int-a1">OK</button>
        <button class="bg-int-white">Cancel</button>
    </div>
</div>

```scss
@use 'path/to/_ui.scss';
button-gruop($radius: $border-radius)
```

|Argument|Description|Example value|
|---|---|---|
|`$radius`|Borderorder radius|`4px`|
