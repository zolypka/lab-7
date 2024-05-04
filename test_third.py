from third import count_routes

def test_count_routes_case1():
    assert count_routes(3, 3) == 6

def test_count_routes_case2():
    assert count_routes(2, 2) == 2

def test_count_routes_case3():
    assert count_routes(1, 1) == 1