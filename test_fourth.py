from fourth import min_edit_distance

def test_min_edit_distance_case1():
    assert min_edit_distance("kitten", "sitting") == 3

def test_min_edit_distance_case2():
    assert min_edit_distance("intention", "execution") == 5

def test_min_edit_distance_case3():
    assert min_edit_distance("abc", "def") == 3