import pytest
import leetcode.may_challenge.day_02_stones_jewels as stones_jewels

@pytest.mark.parametrize("J, S, output", [("aA","aAAbbbb", 3),("z","ZZ", 0)])
def test_stone_jewels_positive_scenario(J, S, output):
    assert(output == stones_jewels.stub(J, S))
