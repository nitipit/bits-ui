# Tag

## Preview
---
<div class="preview-tag" style="display: flex; justify-content: center;">
    <pkt-tag class="bg-a1">tag</pkt-tag>
    <pkt-tag>tag</pkt-tag>
    <pkt-tag class="bg-a2">tag</pkt-tag>
    <pkt-tag class="bg-t1">tag</pkt-tag>
    <pkt-tag class="bg-c">tag</pkt-tag>
    <pkt-tag class="bg-t2">tag</pkt-tag>
</div>

## Usage
---
```html
<pkt-tag>tag</pkt-tag>
```

## SCSS
```scss
@use 'path/to/_ui.scss';

pkt-tag {
    @include ui.tag(
        $bg-color: orange,
        $radius: 4px);
}
```

# Tag-X

## Preview
---
<div class="preview-tag" style="display: flex; justify-content: center;">
    <pkt-tag-x class="bg-a1">one</pkt-tag-x>
    <pkt-tag-x class="bg-p">two</pkt-tag-x>
    <pkt-tag-x class="bg-a2">three</pkt-tag-x>
    <pkt-tag-x class="bg-t1">four</pkt-tag-x>
    <pkt-tag-x class="bg-c">five</pkt-tag-x>
    <pkt-tag-x class="bg-t2">six</pkt-tag-x>
</div>

## Usage
---
```html
<pkt-tag-x>tag</pkt-tag-x>
```

## SCSS
---
```scss
@use 'path/to/_ui.scss';

pkt-tag {
    @include ui.tag(
        $bg-color: orange,
        $radius: 4px)
```
