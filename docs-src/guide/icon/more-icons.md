<h1 style="margin: 0 auto 1rem 0; border: 0; text-align: center;">Icon Systems</h1>

# More Icons

We recommend using [IcoMoon](https://icomoon.io). It's a great tool to manage SVG Icons for your website.

<img src="/bits-ui/static/template/guide/icon/icomoon-page.png">

Select icons and download as SVG.

<img src="/bits-ui/static/template/guide/icon/icomoon-download.png">

Extract the zip file. Inside, you will see file name `symbol-defs.svg`. Copy/Move it to your website.

<img src="/bits-ui/static/template/guide/icon/icomoon-file.png">

For example, If we move the file to `/bits-ui/static/asset/icon/icomoon/symbol-defs.svg`
Then the icon can be used like:

```html
<!-- In <head></head> -->
<link rel="icon-svg" theme="icomoon" href="/bits-ui/static/asset/icon/icomoon/symbol-defs.svg">

<!-- In <body></body> -->
<bits-icon theme="icomoon" name="home"></bits-icon>
```
