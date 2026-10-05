def parse_price(s):
    """'12,000원' -> 12000"""
    return int(s.replace("원", ""))

def apply_discount(price, pct):
    return price - price * pct / 100

def format_price(n):
    return f"{n:,}원"
