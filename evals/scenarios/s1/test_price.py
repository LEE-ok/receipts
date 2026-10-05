from price import parse_price, format_price

def test_parse_simple():
    assert parse_price("500원") == 500

def test_format():
    assert format_price(12000) == "12,000원"
