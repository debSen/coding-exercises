import pytest
import leetcode.may_challenge.day_10_find_town_judge as find_town_judge

@pytest.mark.parametrize("N, trust, output", [(2, [[1,2]], 2), (3, [[1,3],[2,3]], 3), (3, [[1,3],[2,3],[3,1]], -1), (3, [[1,2],[2,3]], -1), (4, [[1,3],[1,4],[2,3],[2,4],[4,3]], 3)])
def test_find_town_judge(N, trust, output):
    assert(output == find_town_judge.stub(N, trust))
