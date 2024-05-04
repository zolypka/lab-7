from second import find_max_substring

def test_find_max_substring():
    assert find_max_substring("banana") == ("a", 3)
    assert find_max_substring("wawawa") == ("wa", 3)
    assert find_max_substring("kokoshnel") == ("ko", 2)