# Tab

## Preview
---
<div id="preview" class="pkt-button-group">
    <pkt-tab>
        <input type="radio" name="tab">
        <button>Tab 1</button>
    </pkt-tab>
    <pkt-tab>
        <input type="radio" name="tab">
        <button>Tab 2</button>
    </pkt-tab>
    <pkt-tab>
        <input type="radio" name="tab">
        <button>Tab 3</button>
    </pkt-tab>
</div>

## Usage
---
```html
<pkt-tab>
    <input type="radio" name="tab">
    <button>Tab 1</button>
</pkt-tab>
<pkt-tab>
    <input type="radio" name="tab">
    <button>Tab 2</button>
</pkt-tab>
<pkt-tab>
    <input type="radio" name="tab">
    <button>Tab 3</button>
</pkt-tab>
```

> <pkt-icon set="adwaita" name="dialog-information"></pkt-icon> `<pkt-tab>` can be wrapped in `<pkt-button-group>`

## SCSS
---

```scss
@use 'path/to/_ui.scss';

pkt-tab {
    @include ui.tab(
        $button-color: grey,
        $highlight-color: orange)
}
```

|Argument|Description|Example Value|
|---|---|---|
|`$button-color`|Button color|`red` `blue`|
|`$highlight-color`|Bottom border color when active|`red` `blue`|
