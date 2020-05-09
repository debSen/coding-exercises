import pytest
import leetcode.may_challenge.day_09_perfect_square as perfect_square

@pytest.mark.parametrize("num, output", [(16, True), (24, False), (81, True), (1, True), (0, True), (2, False)])
def test_perfect_square(num, output):
    assert(output == perfect_square.stub(num))
