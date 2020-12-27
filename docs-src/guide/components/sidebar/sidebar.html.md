# Sidebar

<div id="preview" style="text-align: center; margin-top: 2rem;">
    <span data-id="menu" class="pkt-button-pin" style="font-size: 3rem;">
        <pkt-icon set="adwaita" name="view-dual"></pkt-icon>
    </span>
</div>

## Usage
---
```html
<!-- In <head></head> section. -->
<script>
var sidebar = null // declare `sidebar` as global variable
window.addEventListener('load', function(){
    sidebar = document.querySelector('pkt-sidebar')
    var sidebar_button = document.querySelector('#sidebar-button');
    sidebar_button.addEventListener('click', function(){
        sidebar.show_sidebar();
    });
});
</script>
```

```html
<!-- In <body></body> section. -->
<span id="sidebar-button" class="pkt-button-pin">
    <pkt-icon set="adwaita" name="open-menu"></pkt-icon>
</span>

<pkt-sidebar show="1000px">
    <div el="wrapper" style="background-color: white;">
        <!-- Sidebar contents -->
    </div>
    <div el="overlay"></div>
</pkt-sidebar>
```

## Attributes
---
Attr|Description|Example
--- | --- | ---
show | Minimum screen width to show sidebar | `1000px`


## API
---
`show_sidebar()` : Show sidebar.  
`show_sidebar_no_overlay()` : Show sidebar without overlay.  
`hide_sidebar()` : Hide sidebar.

### Example in Javascript
```javascript
var sidebar = document.querySelector('pkt-sidebar');

sidebar.show_sidebar();
sidebar.hide_sidebar();
sidebar.show_sidebar_no_overlay();
```