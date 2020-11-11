<h1 style="margin: 0; border: 0; text-align: center;">Checkbox</h1>

# Preview
<div data-is="ui" class="flex">
    <bits-checkbox class="size-1 c-c">
        <input type="checkbox" checked>
    </bits-checkbox>
    <bits-checkbox class="size-2 c-t2">
        <input type="checkbox" checked>
    </bits-checkbox>
    <bits-checkbox class="size-3 c-a1">
        <input type="checkbox" checked>
    </bits-checkbox>
    <bits-checkbox class="size-4 c-p">
        <input type="checkbox" checked>
    </bits-checkbox>
    <bits-checkbox class="size-3 c-a2">
        <input type="checkbox" checked>
    </bits-checkbox>
    <bits-checkbox class="size-2 c-t1">
        <input type="checkbox" checked>
    </bits-checkbox>
    <bits-checkbox class="size-1 c-c">
        <input type="checkbox" checked>
    </bits-checkbox>
</div>

# Usage

```html
<bits-checkbox></bits-checkbox>
<bits-checkbox>
    <input type="checkbox" checked>
</bits-checkbox>
```

# Stylus

```stylus
checkbox(
    $bg-color: lighten(grey, 50%), // Inactive background color
    $color-active: $ui-color) // Active & Hover color
```

|Argument|Description|Example value|
|---|---|---|
|`$bg-color`|Background color : Color supported by **CSS**, **Stylus** or **Bits UI Color**|`red` `$color-p`|
|`$color-active`|Background color for **active** and **hover** state|`red` `$color-p` `#AAA`|
