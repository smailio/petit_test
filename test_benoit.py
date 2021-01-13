def find_secret():
    pass


def test_find_secret():
    assert find_secret("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
    assert find_secret("hello world!") == ""


def my_name_is(text):
    return ""


def test_my_name_is():
    assert (
        my_name_is("Je m'appele Anis. j'ai 26 ans. je passe un test")
        == "Je m'appelle Benoit. j'ai 26 ans. je passe un test"
    )


def reverse_string():
    pass


def test_reverse_string():
    assert reverse_string("abcde") == "edcba"
    assert reverse_string("aaa") == "aaa"
    assert reverse_string("aaaeee") == "eeeaaa"
    assert reverse_string("a") == "a"
    assert reverse_string("") == ""


def transpose():
    pass


def test_transpose():
    assert transpose([[1, 2], ["a", "b"]]) == [(1, "a"), (2, "b")]
    assert transpose([[1, 2, 3], ["a", "b", "c"]]) == [(1, "a"), (2, "b"), (3, "c")]
