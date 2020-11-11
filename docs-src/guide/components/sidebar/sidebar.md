<h1 style="margin: 0; border: 0; text-align: center;">Sidebar</h1>

<div id="preview" style="text-align: center; margin-top: 2rem;">
    <span data-id="menu" class="bits-button-pin" style="font-size: 3rem;">
        <bits-icon theme="adwaita" name="open-menu"></bits-icon>
    </span>
</div>

# Usage
```html
<!-- In <head></head> section. -->
<script>
var sidebar = null // declare `sidebar` as global variable
window.addEventListener('load', function(){
    sidebar = document.querySelector('bits-sidebar')
    var sidebar_button = document.querySelector('#sidebar-button');
    sidebar_button.addEventListener('click', function(){
        sidebar.show_sidebar();
    });
});
</script>
```

```html
<!-- In <body></body> section. -->
<span id="sidebar-button" class="bits-button-pin">
    <bits-icon theme="adwaita" name="open-menu"></bits-icon>
</span>

<bits-sidebar show="1000px">
    <div el="wrapper" style="background-color: white;">
        <!-- Sidebar contents -->
    </div>
    <div el="overlay"></div>
</bits-sidebar>
```

# API
`show_sidebar()` Show sidebar  
`hide_sidebar()` Hide sidebar