import pytest
import leetcode.may_challenge.day_06_majority_element as majority_element

@pytest.mark.parametrize("nums, output", [([3,2,3],3),([1,1],1),([2,2,1,1,1,2,2],2)])
def test_majority_element(nums, output):
    assert(output == majority_element.stub(nums))
