<h1 style="margin: 0; border: 0; text-align: center;">Table</h1>

<h2 style="text-align: center;"><tag>Styled Element</tag></h2>

# Preview
|Column 1|Column 2|Column 3|
|---|---|---|
|11|12|13|
|21|22|23|
|31|32|33|

# Usage
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

# Stylus
```stylus
table(
        $bg-color: $color-a2,
        $border-vertical: true,
        $border-horizontal: true)
```
