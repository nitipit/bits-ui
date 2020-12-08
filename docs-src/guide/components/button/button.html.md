# Buttons

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


## Button
---
<button>Button</button>
```html
<button>button</button>
<a class="button">button</a>
```

### SCSS
```scss
@use 'path/to/_ui.scss';

button {
    @include ui.button($bg-color: orange, $radius: 4px);
}
```

|Argument|Description|Example value|
|---|---|---|
|`$bg-color`|Background color|`red`|
|`$radius`|Border radius|`4px`|


## Pin
---
<span class="pkt-button-pin">+</span>
```html
<pkt-button-pin>+</pkt-button-pin>
<a class="pkt-button-pin">+</a>
```

### SCSS
```scss
@use 'path/to/_ui.scss';

pkt-button-pin {
    @include ui.button-pin($bg-color: $ui-color);
}
```

|Argument|Description|Example value|
|---|---|---|
|`$bg-color`|Background color|`red`|


## Square Button
---
<span class="pkt-button-square">+</span>

```html
<pkt-button-square>+</pkt-button-square>
<a class="pkt-button-square">+</a>
```

### SCSS
```scss
@use 'path/to/_ui.scss';

pkt-button-square {
    @include ui.button-square($bg-color: $ui-color);
}
```

|Argument|Description|Example value|
|---|---|---|
|`$bg-color`|Background color|`red`|

## Group Button
---
Grouping buttons together. Can apply to `button` and `pkt-button-square`

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

### SCSS
```scss
@use 'path/to/_ui.scss';

pkt-button-group {
    @include ui.button-group($radius: 4px);
}
```

|Argument|Description|Example value|
|---|---|---|
|`$radius`|Border radius|`4px`|
