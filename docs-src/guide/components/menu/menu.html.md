# Menu

## Preview
---

<div id="preview">
    <pkt-menu>
    <ul>
        <li>
            <a>1</a>
            <ul>
                <li>
                    <a>1-1</a>
                    <ul>
                        <li><a>1-1-1</a></li>
                        <li><a>1-1-2</a></li>
                    </ul>
                </li>
                <li>
                    <a>1-2</a>
                    <ul>
                        <li><a>1-2-1</a></li>
                    </ul>
                </li>
            </ul>
        </li>
        <li>
            <a>2</a>
            <ul>
                <li>
                    <a>2-1</a>
                    <ul>
                        <li><a>2-1-1</a></li>
                    </ul>
                </li>
                <li>
                    <a>2-2</a>
                </li>
            </ul>
        </li>
    </ul>
    </pkt-menu>
</div>

## Usage
---
```html
<pkt-menu><ul>
    <li>
        <a>1</a>
        <ul>
            <li>
                <a>1-1</a>
                <ul>
                    <li><a>1-1-1</a></li>
                    <li><a>1-1-2</a></li>
                </ul>
            </li>
            <li>
                <a>1-2</a>
                <ul>
                    <li><a>1-2-1</a></li>
                </ul>
            </li>
        </ul>
    </li>
    <li>
        <a>2</a>
        <ul>
            <li>
                <a>2-1</a>
                <ul>
                    <li><a>2-1-1</a></li>
                </ul>
            </li>
            <li>
                <a>2-2</a>
            </li>
        </ul>
    </li>
</ul></pkt-menu>
```

## SCSS
---

```scss
@use 'path/to/_ui.scss';

pkt-menu {
    @include ui.menu(
        $border-color: orange,
        $active-color: orange,
        $arrow-color: orange)
}
```

|Argument|Description|Example|
|---|---|---|
|`$border-color`|Border color : Color supported by **CSS**, **Stylus** or **Bits UI Color**|`red` `$color-p` `#AAA`|
|`$active-color`|Active color on click : Color supported by **CSS**, **Stylus** or **Bits UI Color**|`red` `$color-p` `#AAA`|
|`$arrow-color`|Arrow color : Color supported by **CSS**, **Stylus** or **Bits UI Color**|`red` `$color-p` `#AAA`|
