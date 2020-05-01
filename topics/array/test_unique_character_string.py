import pytest
import topics.array.unique_character_string as unique_character_string

@pytest.mark.parametrize("str", ["abc", "", "a1b2c3", "a. *!@#$%^", "1234567890"])
def test_unique_string_positive_scenario(str):
    assert(unique_character_string.is_unique_char_string(str))

@pytest.mark.parametrize("str", ["abc"])
def test_unique_string_multiple_string(str):
    with pytest.raises(TypeError, match=r"positional"):    
        assert(unique_character_string.is_unique_char_string(str, str))

@pytest.mark.parametrize("str", ["abcc", "111", "abbc", "aaaaaaa", "  "])
def test_unique_string_negative(str):
    assert not unique_character_string.is_unique_char_string(str)
