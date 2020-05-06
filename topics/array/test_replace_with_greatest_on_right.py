import pytest
import topics.array.replace_with_greatest_on_right as replace_with_greatest_on_right

@pytest.mark.parametrize("arr, output", [([17,18,5,4,6,1], [18,6,6,6,1,-1])])
def test_replace_with_greatest_on_right_positive_scenario(arr, output):
    assert (output == replace_with_greatest_on_right.stub(arr))

