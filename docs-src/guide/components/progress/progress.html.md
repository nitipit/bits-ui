# Progress

## Dot Pulse
---
<pkt-dotpulse></pkt-dotpulse>

### Usage

```html
<pkt-dotpulse></pkt-dotpulse>
```

### SCSS
```scss
@use 'path/to/_ui.scss';

@include ui.pkt-dotpulse($color: orange) // Dot pulse color
```

## Progress Bar
---
<pkt-progress-bar style="margin-top: 2rem;"></pkt-progress-bar>
<pkt-progress-bar class="a1" value="25%" style="margin-top: 2rem;"></pkt-progress-bar>

### Usage
```html
<pkt-progress-bar></pkt-progress-bar>
<pkt-progress-bar value="25%"></pkt-progress-bar>
```

### Attributes
|Attr.|Description|Example|
|---|---|---|
|`value`|Value in percentage from "0%" to "100%"|`value="25%"`|


### SCSS

```scss
@use 'path/to/_ui.scss';

pkt-progress-bar {
    @include ui.progress-bar($color: orange) // Progress bar color
}
```

## Spinner
---
<div>
    <pkt-spinner></pkt-spinner>
</div>

### Usage
```html
<pkt-spinner></pkt-spinner>
```

### SCSS
```scss
@use 'path/to/_ui.scss';

pkt-spinner {
    @include ui.spinner($color: $ui-color) // Spinner color
}
```
