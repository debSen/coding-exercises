import pytest
import topics.array.valid_mountain_Array as valid_mountain_Array

@pytest.mark.parametrize("A", [[0,3,2,1]])
def test_valid_mountain_Array_positive_scenario(A):
    assert valid_mountain_Array.stub(A)

@pytest.mark.parametrize("A", [[2,1],
                                       [3,5,5],
                                       [0,1,2,3,4,5,6,7,8,9],
                                       [9,8,7,6,5,4,3,2,1,0]])
def test_valid_mountain_Array_negative_scenario(A):
    assert not valid_mountain_Array.stub(A)
