<h1 style="margin: 0; border: 0; text-align: center;">Input</h1>

# Text, Email, Password, etc.
<div class="p">
    <input type="text" placeholder="Text">
    <input type="email" placeholder="Email">
    <input type="password" placeholder="Password">
</div>

```html
<input type="text" placeholder="Text">
<input type="email" placeholder="Email">
<input type="password" placeholder="Password">
```

# Number Input
<bits-input-number>
    <input type="number" max="1000" min="0">
</bits-input-number>

```html
<bits-input-number></bits-input-number>

<!-- Customized input -->
<bits-input-number>
    <input type="number" max="1000" min="0">
</bits-input-number>
```

# Radio Input

<div class="p">
    <bits-input-radio>
        <input type="radio" name="gender" value="m">
    </bits-input-radio>
    <span>Male</span>
    <bits-input-radio>
        <input type="radio" name="gender" value="f">
    </bits-input-radio>
    <span>Female</span>
</div>

<div class="bits-button-group" style="margin-top: 2rem;">
    <bits-input-radio-btn>
        <input type="radio" name="position" value="left">
        <button>Left</button>
    </bits-input-radio-btn>
    <bits-input-radio-btn>
        <input type="radio" name="position" value="center">
        <button>Center</button>
    </bits-input-radio-btn>
    <bits-input-radio-btn>
        <input type="radio" name="position" value="center">
        <button>Right</button>
    </bits-input-radio-btn>
</div>

## Usage
```html
<bits-input-radio>
    <input type="radio" name="gender" value="m">
</bits-input-radio>
<span>Male</span>
<bits-input-radio>
    <input type="radio" name="gender" value="f">
</bits-input-radio>
<span>Female</span>
```

```html
<bits-button-group>
    <bits-input-radio-btn>
        <input type="radio" name="position" value="left">
        <button>Left</button>
    </bits-input-radio-btn>
    <bits-input-radio-btn>
        <input type="radio" name="position" value="center">
        <button>Center</button>
    </bits-input-radio-btn>
    <bits-input-radio-btn>
        <input type="radio" name="position" value="center">
        <button>Right</button>
    </bits-input-radio-btn>
</bits-button-group>
```

# Range Input

<input type="range" style="min-width: 200px; width: 50%">

## Usage

```html
<input type="range">
```

## Stylus
```stylus
slider(
    $thumb-color: lighten(grey, 80%),
    $thumb-color-active: $ui-color,
    $bar-color: lighten(grey, 50%))
```

|Argument|Description|Example value|
|---|---|---|
|`$thumb-color`|Slider's thumb color : Color supported by **CSS**, **Stylus** or **Bits UI Color**|`red` `$color-p` `#AAA`|
|`$thumb-color-active`|Slider's thumb color for **active** and **hover** state|`red` `$color-p` `#AAA`|
|`$bar-color`|Slider's bar color|`red` `$color-p` `#AAA`|


# Tag Input
<div class="p">
    <bits-input-tag></bitsinput-tag>
</div>

## Usage

```html
<bits-input-tag></bits-input-tag>
```

## API
|API|Description|
|---|---|
|`add_tag(value)`|Add `value` as a tag|
|`get_tags()`|Get tag list from input|
