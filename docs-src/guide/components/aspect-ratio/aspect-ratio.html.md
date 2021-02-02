# Aspect Ratio

Aspect Ratio Box is essential for multimedia such as videos, movies or
card like contents.

Refer to [https://css-tricks.com/aspect-ratio-boxes/](https://css-tricks.com/aspect-ratio-boxes/)

## Preview
---
<div id="preview">
    <div class="box" style="--aspect-ratio:1;">1:1</div>
    <div class="box" style="--aspect-ratio:4/3;">4:3</div>
    <div class="box" style="--aspect-ratio:16/9;">16:9</div>
    <div class="box" style="--aspect-ratio:21/9;">21:9</div>
</div>

## Use Case
---
Responsive video with `21:9` aspect ratio ? ;)
<div class="video" style="--aspect-ratio:21/9;">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/WhWc3b3KhnY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Usage
---

```html
<div style="--aspect-ratio:1;">1:1</div>
<div style="--aspect-ratio:4/3;">4:3</div>
<div style="--aspect-ratio:16/9;">16:9</div>
<div style="--aspect-ratio:21/9;">21:9</div>
```