import module as m

# 100000 -100000
# 0
# 1 -1
# 100 -100


def test_add_100000():
    assert m.add(100000, 100000) == 200000


def test_neg_100000():
    assert m.add(-100000, -100000) == -200000


def test_add_zero():
    assert m.add(0, 0) is None


def test_add_1():
    assert m.add(1, 1) == 2


def test_neg_1():
    assert m.add(-1, -1) == -2


def test_add_100():
    assert m.add(100, 100) == 200


def test_neg_100():
    assert m.add(-100, -100) == -200
