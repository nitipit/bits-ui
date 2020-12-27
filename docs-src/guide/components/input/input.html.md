# Input

## Text, Email, Password, etc.
---
<div>
    <input type="text" placeholder="Text">
    <input type="email" placeholder="Email">
    <input type="password" placeholder="Password">
</div>

```html
<input type="text" placeholder="Text">
<input type="email" placeholder="Email">
<input type="password" placeholder="Password">
```

## Number Input
---
<pkt-input-number>
    <input type="number" max="1000" min="0">
</pkt-input-number>

```html
<pkt-input-number></pkt-input-number>

<!-- Customized input -->
<pkt-input-number>
    <input type="number" max="1000" min="0">
</pkt-input-number>
```

## Radio Input
---
<div>
    <pkt-input-radio>
        <input type="radio" name="gender" value="m">
    </pkt-input-radio>
    <span>Male</span>
    <pkt-input-radio>
        <input type="radio" name="gender" value="f">
    </pkt-input-radio>
    <span>Female</span>
</div>

<div class="pkt-button-group" style="margin-top: 2rem;">
    <pkt-input-radio-btn>
        <input type="radio" name="position" value="left">
        <button>Left</button>
    </pkt-input-radio-btn>
    <pkt-input-radio-btn>
        <input type="radio" name="position" value="center">
        <button>Center</button>
    </pkt-input-radio-btn>
    <pkt-input-radio-btn>
        <input type="radio" name="position" value="center">
        <button>Right</button>
    </pkt-input-radio-btn>
</div>


```html
<pkt-input-radio>
    <input type="radio" name="gender" value="m">
</pkt-input-radio>
<span>Male</span>
<pkt-input-radio>
    <input type="radio" name="gender" value="f">
</pkt-input-radio>
<span>Female</span>
```

```html
<pkt-button-group>
    <pkt-input-radio-btn>
        <input type="radio" name="position" value="left">
        <button>Left</button>
    </pkt-input-radio-btn>
    <pkt-input-radio-btn>
        <input type="radio" name="position" value="center">
        <button>Center</button>
    </pkt-input-radio-btn>
    <pkt-input-radio-btn>
        <input type="radio" name="position" value="center">
        <button>Right</button>
    </pkt-input-radio-btn>
</pkt-button-group>
```

## Range Input
---

<div style="display: flex; justify-content: center;">
    <input type="range" style="min-width: 200px; width: 50%;
        margin-top: 3rem; margin-bottom: 2rem;">
</div>

### Usage

```html
<input type="range">
```

### SCSS

```scss
@use 'path/to/_ui.scss';

input[type="range"] {
    @include ui.slider(
        $thumb-color: grey,
        $thumb-color-active: orange,
        $bar-color: grey)
}
```

|Argument|Description|Example value|
|---|---|---|
|`$thumb-color`|Slider's thumb color : Color supported by **CSS**, **Stylus** or **Bits UI Color**|`red` `#AAA`|
|`$thumb-color-active`|Slider's thumb color for **active** and **hover** state|`red` `#AAA`|
|`$bar-color`|Slider's bar color|`red` `#AAA`|


## Tag Input
---
<div style="margin-top: 2rem;">
    <pkt-input-tag></bitsinput-tag>
</div>

### Usage

```html
<pkt-input-tag></pkt-input-tag>
```

### API
|API|Description|
|---|---|
|`add_tag(value)`|Add `value` as a tag|
|`tags`|Get tag list from input|
