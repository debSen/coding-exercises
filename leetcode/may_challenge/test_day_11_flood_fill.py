import pytest
import leetcode.may_challenge.day_11_flood_fill as flood_fill

@pytest.mark.parametrize("image, sr, sc, newColor, output", [([[1,1,1],[1,1,0],[1,0,1]], 1,1,2, [[2,2,2],[2,2,0],[2,0,1]])])
def test_flood_fill(image, sr, sc, newColor, output):
    assert(output == flood_fill.stub(image, sr, sc, newColor))
