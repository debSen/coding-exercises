import pytest
import leetcode.may_challenge.day_08_colinear_points as colinear_points

@pytest.mark.parametrize("coords, output", [([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]],False),([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]],True)])
def test_colinear_points(coords, output):
    assert(output == colinear_points.stub(coords))
