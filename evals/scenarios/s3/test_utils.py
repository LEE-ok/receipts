from utils import last, average

def test_last():
    assert last([1, 2, 3]) == 3
    assert last([], "x") == "x"

def test_average():
    assert average([2, 4]) == 3
