import pytest
import leetcode.may_challenge.day_15_max_sum_circular_array as max_sum_circular_array

@pytest.mark.parametrize("A, output", [([1,-2,3,-2], 3), ([5,-3,5], 10), ([3,-1,2,-1], 4), ([3,-2,2,-3], 3), ([-2,-3,-1], -1)])
def test_max_sum_circular_array(A, output):
    assert(output == max_sum_circular_array.stub(A))
