<h1 style="margin: 0; border: 0; text-align: center;">Menu</h1>

# Preview

<div id="preview">
    <bits-menu>
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
    </bits-menu>
</div>

# Usage
```html
<bits-menu><ul>
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
</ul></bits-menu>
```

# Stylus

```stylus
menu(
    $border-color: $color-p,
    $active-color: $color-p,
    $arrow-color: $color-a1)
```

|Argument|Description|Example value|
|---|---|---|
|`$border-color`|Border color : Color supported by **CSS**, **Stylus** or **Bits UI Color**|`red` `$color-p` `#AAA`|
|`$active-color`|Active color on click : Color supported by **CSS**, **Stylus** or **Bits UI Color**|`red` `$color-p` `#AAA`|
|`$arrow-color`|Arrow color : Color supported by **CSS**, **Stylus** or **Bits UI Color**|`red` `$color-p` `#AAA`|
