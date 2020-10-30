<h1 style="margin: 0; border: 0; text-align: center;">Slide</h1>

<div id="preview" style="text-align: center; margin-top: 3rem;">
    <bits-slide>
        <img class="slide" src="/bits-ui/static/template/guide/components/slide/dessert-1.jpg">
        <img class="slide" src="/bits-ui/static/template/guide/components/slide/dessert-2.jpg">
        <img class="slide" src="/bits-ui/static/template/guide/components/slide/dessert-3.jpg">
    </bits-slide>
</div>

# Usage
```html
<bits-slide>
    <div class="slide"></div>
    <div class="slide"></div>
    <div class="slide"></div>
</bits-slide>
```

# Manual setup
```html
<bits-slide manual>
    <div class="slide"></div>
    <div class="slide"></div>
    <div class="slide"></div>
</bits-slide>

<script>
window.addEventListener('load', () => {
    document.querySelector('bits-slide').setup({
        duration: 300,
        easing: 'ease-out',
        perPage: 1,
        startIndex: 0,
        draggable: true,
        multipleDrag: true,
        threshold: 20,
        loop: true,
        rtl: false
    })
})
</script>
```

Manual options are the same as Siema. See [Siema Options](https://pawelgrzybek.github.io/siema/#options) for details.
