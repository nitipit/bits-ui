# Switch

## Preview
---
<div data-id="preview" style="font-size: 1.5rem; display: flex;">
    <pkt-switch></pkt-switch>
    <pkt-switch class="color-a2">
        <input type="checkbox">
        <div el="label">
            <span>YES</span>
            <span>NO</span>
        </div>
    </pkt-switch>
</div>

## Usage
---
```html
<pkt-switch></pkt-switch>

<pkt-switch>
    <input type="checkbox">
    <div el="label">
        <span>YES</span>
        <span>NO</span>
    </div>
</pkt-switch>
```

## SCSS
---
```scss
@use 'path/to/_ui.scss';

pkt-switch {
    @include ui.switch($color-active: orange);
}
```
