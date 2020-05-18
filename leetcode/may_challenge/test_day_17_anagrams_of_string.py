import pytest
import leetcode.may_challenge.day_17_anagrams_of_string as anagrams_of_string

@pytest.mark.parametrize("s,p, output", [("cbaebabacd", "abc", [0,6]), ("abab", "ab", [0,1,2])])
def test_anagrams_of_string(s,p, output):
    assert(output == anagrams_of_string.stub(s,p))
