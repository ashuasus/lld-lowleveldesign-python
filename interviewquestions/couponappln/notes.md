# Coupon Application — Notes

## Design Patterns Used
- **Decorator** — `CouponDecorator` wraps a `Product` and overrides `get_price()` to apply a discount; decorators chain so a product can have multiple coupons stacked on top of each other
- **Factory Method (implicit)** — `ShoppingCart.add_to_cart()` hard-codes the decorator stack: `TypeCouponDecorator(PercentageCouponDecorator(product, 20), 10)`, acting as the single place that controls which coupons are applied

## Key Classes
- `Product` — abstract base with `name`, `original_price`, `type`, and abstract `get_price()`
- `Item1` / `Item2` / `Item3` / `Item4` — concrete products; `get_price()` returns `original_price` directly
- `CouponDecorator` — abstract decorator; extends `Product` and stores the wrapped `product` reference
- `PercentageCouponDecorator` — applies a flat percentage discount on whatever the inner `product.get_price()` returns
- `TypeCouponDecorator` — applies a percentage discount only if the product type is in an eligible list (`FURNITURE`, `ELECTRONICS`); otherwise passes price through unchanged
- `ShoppingCart` — wraps each added product in the decorator stack; `get_total_price()` calls `get_price()` on each decorated product

## Things to Remember
- **Decorator chain ordering matters** — `TypeCouponDecorator(PercentageCouponDecorator(product, 20), 10)` means: first apply 20% off (inner), then apply a type-specific 10% off on the already-discounted price (outer). Reversing the order would produce a different total for eligible types.
- **`TypeCouponDecorator` wraps the inner decorator, not the raw product** — so when `TypeCouponDecorator.get_price()` calls `self.product.get_price()`, it actually calls `PercentageCouponDecorator.get_price()`, which already has 20% applied. The type discount then stacks on top of that reduced price.
- **Non-eligible products skip the type discount silently** — `TypeCouponDecorator.get_price()` returns `price` unchanged for `PHARMACY` and `CLOTHES` types. The percentage coupon still applies to all products though.
- **`CouponDecorator.__init__` calls `product.get_price()` as the initial price** — actually it passes `product.get_price()` as the `price` argument to `super().__init__`, but this `original_price` is never used by the decorators; they always delegate to `self.product.get_price()` dynamically. The stored `original_price` in the decorator is effectively unused.
- **Decorators are constructed at `add_to_cart()` time** — coupons are fixed at cart-insertion time, not at checkout. Changing coupon rules after adding items would require re-adding the products.
- **`eligible_types` is a class variable on `TypeCouponDecorator`** — it's shared across all instances, acting as a configuration list. In production this would be injected or loaded from config.
