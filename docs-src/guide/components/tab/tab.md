<h1 style="margin: 0; border: 0; text-align: center;">Tab</h1>

<h2 style="text-align: center;"><tag>Styled Element</tag></h2>

# Preview
<div id="preview" class="bits-button-group">
    <bits-tab>
        <input type="radio" name="tab">
        <button>Tab 1</button>
    </bits-tab>
    <bits-tab>
        <input type="radio" name="tab">
        <button>Tab 2</button>
    </bits-tab>
    <bits-tab>
        <input type="radio" name="tab">
        <button>Tab 3</button>
    </bits-tab>
</div>

# Usage
```html
<bits-tab>
    <input type="radio" name="tab">
    <button>Tab 1</button>
</bits-tab>
<bits-tab>
    <input type="radio" name="tab">
    <button>Tab 2</button>
</bits-tab>
<bits-tab>
    <input type="radio" name="tab">
    <button>Tab 3</button>
</bits-tab>
```

> <div class="bits-tag">Note</div> `<bits-tab>` Can be wrapped in `<bits-button-group>`

# Stylus

```stylus
tab(
    $button-color: lighten(grey, 70%),
    $highlight-color: $ui-color)
```

|Argument|Description|Example value|
|---|---|---|
|`$button-color`|Button color|`red` `blue`|
|`$highlight-color`|Bottom border color on active|`red` `blue`|
