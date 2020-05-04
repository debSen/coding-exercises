import pytest
import leetcode.may_challenge.day_03_number_compliment as number_compliment

@pytest.mark.parametrize("num, output", [(5,2),(1,0)])
def test_number_compliment_positive_scenario(num, output):
    assert(output == number_compliment.stub(num))
