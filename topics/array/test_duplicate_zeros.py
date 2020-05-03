import pytest
import topics.array.duplicate_zeros as duplicate_zeros

@pytest.mark.parametrize("arr, output", [([1,0,2,3,0,4,5,0], [1,0,0,2,3,0,0,4]), ([1,2,3], [1,2,3])])
def test_duplicate_zeros_positive_scenario(arr, output):
    assert(output == duplicate_zeros.stub(arr))
