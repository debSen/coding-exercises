import pytest
import leetcode.may_challenge.day_01_first_bad_version as first_bad_version

@pytest.mark.parametrize("n, version", [(5, 1), (1,1), (2,1), (4,2), (10,10)])
def test_unique_string_positive_scenario(n, version):
    assert(version == first_bad_version.stub(n, version))

