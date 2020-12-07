<h1 style="border: 0; margin: 0; text-align: center;">Box Arrow</h1>

## Preview
---
<div id="preview">
    <div>
        <span class="pkt-box-arrow top">Arrow Top</span>
        <span class="pkt-box-arrow right">Arrow Right</span>
        <span class="pkt-box-arrow bottom">Arrow Bottom</span>
        <span class="pkt-box-arrow left">Arrow Left</span>
    </div>
    <div>
        <p class="pkt-box-arrow top">
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        </p>
    </div>
</div>

## Usage
---
```html
<span class="pkt-box-arrow-top">Arrow Top</span>
<span class="pkt-box-arrow-right">Arrow Right</span>
<span class="pkt-box-arrow-bottom">Arrow Bottom</span>
<span class="pkt-box-arrow-left">Arrow Left</span>
```

## SCSS
---
```scss
@use 'sass:color';
@use 'path/to/_ui.scss';

@include ui.box-arrow(
    $arrow: top,
    $arrow-size: 7px,
    $position: 50%,
    $bg-color: color.adjust(white, $lightness: -20%),
    $border-width: 1px,
    $border-color: black,
    $radius: var.$border-radius)
```

|Argument|Description|Example value|
|---|---|---|
|`$arrow`|Arrow position and direction : `top`, `right`, `bottom`, `left`|`top`|
|`$arrow-size`|Arrow size apply to width & height : can be any CSS size unit|`7px` `2em`|
|`$position`|Arrow position : any css size unit |`50%` `10px`|
|`$bg-color`|Background color|`orange`|
|`$border-width`|Border width|`1px` `2px`|
|`$border-color`|Border color|`red`|
