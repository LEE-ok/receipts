from cart import total

def test_no_coupon():
    assert total([(10, 2), (5, 1)]) == 25

def test_coupon_upper():
    assert total([(10, 1)], "HALF") == 5

def test_coupon_case_insensitive():
    assert total([(10, 1)], "half") == 5
