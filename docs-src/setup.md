## Basic Set Up

To use default style and color, just put codes below in html `<head>` and you're good to go.

```html
<head>
    <!-- Load default CSS -->
    <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/packet-ui@1.0.2/dist/normalize.css">
    <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/packet-ui@1.0.2/dist/packet-ui.css">

    <!-- Load packet-ui.js -->
    <script defer src="https://cdn.jsdelivr.net/npm/packet-ui@1.0.2/dist/packet-ui.js"></script>

    <!-- Set up font for UI components. Cantarell is recommended -->
    <style>
    @font-face {
        font-family: 'packet-ui';
        src: url('https://fonts.gstatic.com/s/cantarell/v10/B50NF7ZDq37KMUvlO015jKJr.woff2') format('woff2');
    }
    </style>
</head>
```

## Usage

Use web components `<pkt-*>` anywhere in html `<body>`, for examples:

```html
<body>
    <pkt-badge></pkt-badge>
    <pkt-switch></pkt-switch>
</body>
```