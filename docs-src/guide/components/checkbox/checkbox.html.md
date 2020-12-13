# Checkbox

## Preview
---
<div data-is="ui" class="flex">
    <pkt-checkbox class="size-1 c-c">
        <input type="checkbox" checked>
    </pkt-checkbox>
    <pkt-checkbox class="size-2 c-t2">
        <input type="checkbox" checked>
    </pkt-checkbox>
    <pkt-checkbox class="size-3 c-a1">
        <input type="checkbox" checked>
    </pkt-checkbox>
    <pkt-checkbox class="size-4 c-p">
        <input type="checkbox" checked>
    </pkt-checkbox>
    <pkt-checkbox class="size-3 c-a2">
        <input type="checkbox" checked>
    </pkt-checkbox>
    <pkt-checkbox class="size-2 c-t1">
        <input type="checkbox" checked>
    </pkt-checkbox>
    <pkt-checkbox class="size-1 c-c">
        <input type="checkbox" checked>
    </pkt-checkbox>
</div>

## Usage
---

```html
<pkt-checkbox></pkt-checkbox>
<pkt-checkbox>
    <input type="checkbox" checked>
</pkt-checkbox>
```

## SCSS

```scss
@use 'path/to/_ui.scss';

@include ui.checkbox(
    $bg-color: grey, // Inactive background color
    $color-active: orange) // Active & Hover color
}
```

|Argument|Description|Example value|
|---|---|---|
|`$bg-color`|inactive background color|`grey` `#AAA`|
|`$color-active`|background color for **active** and **hover** state|`orange`|
