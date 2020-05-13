import pytest
import leetcode.may_challenge.day_12_single_element as single_element

@pytest.mark.parametrize("nums, output", [([1,1,2,3,3,4,4,8,8], 2), ([3,3,7,7,10,11,11], 10)])
def test_single_element(nums, output):
    assert(output == single_element.stub(nums))
