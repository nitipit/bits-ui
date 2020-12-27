# Table

## Preview
---
|Column 1|Column 2|Column 3|
|---|---|---|
|11|12|13|
|21|22|23|
|31|32|33|

## Usage
---
```html
<table>
    <thead>
        <tr>
            <th>Column 1</th>
            <th>Column 2</th>
            <th>Column 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>11</td>
            <td>12</td>
            <td>13</td>
        </tr>
        <tr>
            <td>21</td>
            <td>22</td>
            <td>23</td>
        </tr>
        <tr>
            <td>31</td>
            <td>32</td>
            <td>33</td>
        </tr>
    </tbody>
</table>
```

## SCSS
---
```scss
@use 'path/to/_ui.scss';

table {
    @include ui.table(
        $bg-color: orange,
        $border-vertical: true,
        $border-horizontal: true)
}
```

### Arguments

|Argument|Description|Example Value|
|---|---|---|
|`$bg-color`|background color|`grey` `#AAA`|
|`$border-vertical`|Show vertical line (boolean)|`true` `false`|
|`$border-vertical`|Show horizontal line (boolean)|`true` `false`|