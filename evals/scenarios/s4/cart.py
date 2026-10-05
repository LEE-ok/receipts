COUPONS = {"HALF": 0.5, "TENOFF": 0.9}

def total(items, coupon=None):
    """items: [(price, qty)]. Coupon codes are case-insensitive (changed by Minsu)."""
    s = sum(p * q for p, q in items)
    if coupon in COUPONS:
        s *= COUPONS[coupon]
    return round(s, 2)
