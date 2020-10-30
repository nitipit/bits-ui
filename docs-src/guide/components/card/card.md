<h1 style="margin: 0; border: 0; text-align: center;">Card</h1>

# Preview
<div style="display: flex; justify-content:center;">
    <bits-card style="width: 90%; max-width: 300px;">
        <h2 class="bg-a1 border-top-radius">Dessert</h2>
        <img src="/bits-ui/static/template/guide/components/card/dessert.jpg">
        <p>
            A whole batch of basic vanilla cupcakes, topped with the best
            buttercream I’ve ever ever. If you don’t know how to make anything
            else in your life, at very least, perfect the vanilla cupcake.
        </p>
        <bits-button-group>
            <button class="bg-int-p">
                <bits-icon theme="adwaita" name="emblem-favorite"></bits-icon>
            </button>
            <button class="bg-int-p">
                <bits-icon theme="adwaita" name="emblem-shared"></bits-icon>
            </button>
        </bits-button-group>
    </bits-card>
</div>

# Usage
```html
<bits-card>
    <h2 class="bg-a1 border-top-radius">Dessert</h2>
    <img src="dessert.jpg">
    <p>
        A whole batch of basic vanilla cupcakes, topped with the best
        buttercream I’ve ever ever. If you don’t know how to make anything
        else in your life, at very least, perfect the vanilla cupcake.
    </p>
    <bits-button-group>
        <button class="bg-int-p">
            <bits-icon theme="adwaita" name="emblem-favorite"></bits-icon>
        </button>
        <button class="bg-int-p">
            <bits-icon theme="adwaita" name="emblem-shared"></bits-icon>
        </button>
    </bits-button-group>
</bits-card>
```

> CSS UI class `border-top-radius` or `border-bottom-radius` can be used to make round corner for element inside.

# Stylus
```stylus
card($radius: $border-radius)
```

|Argument|Description|Example value|
|---|---|---|
|`$radius`|Card border radius|`4px`, `1em`|
