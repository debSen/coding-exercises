import pytest
import leetcode.may_challenge.day_18_perm_of_string as perm_of_string

@pytest.mark.parametrize("s1, s2, output", [("ab", "eidbaooo", True), ("ab", "eidboaoo", False)])
def test_perm_of_string(s1, s2, output):
    assert(output == perm_of_string.stub(s1, s2))
