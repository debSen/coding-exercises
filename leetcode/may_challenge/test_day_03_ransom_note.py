import pytest
import leetcode.may_challenge.day_03_ransom_note as ransom_note

@pytest.mark.parametrize("ransomNote, magazine", [("aa", "aab"), ("a", "bbcca")])
def test_ransom_note_positive(ransomNote, magazine):
    assert(ransom_note.stub(ransomNote, magazine))

@pytest.mark.parametrize("ransomNote, magazine", [("a", "b"), ("aa", "ab")])
def test_ransom_note_negative(ransomNote, magazine):
    assert not ransom_note.stub(ransomNote, magazine)
