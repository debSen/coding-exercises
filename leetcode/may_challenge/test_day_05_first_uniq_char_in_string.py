import pytest
import leetcode.may_challenge.day_05_first_uniq_char_in_string as first_uniq_char_in_string

@pytest.mark.parametrize("s, output", [("leetcode",0),("loveleetcode",2), ("", -1)])
def test_first_uniq_char_in_string_positive_scenario(s, output):
    assert(output == first_uniq_char_in_string.stub(s))
