def remove_dup(s: str) -> str:
    new = []
    
    for c in s:
        if new and c == new[-1].swapcase():
            new.pop()
        else:
            new.append(c)
    
    return ''.join(new)


def test_remove_dup():
    assert remove_dup("abBA") == ""
    assert remove_dup("abAB") == "abAB"
    assert remove_dup("aA") == ""
    assert remove_dup("Aa") == ""
    assert remove_dup("aabAAB") == "aabAAB"
    assert remove_dup("abcdef") == "abcdef"
    assert remove_dup("") == ""
    assert remove_dup("a") == "a"
    assert remove_dup("aAbB") == ""


test_remove_dup()
print("All tests passed!")