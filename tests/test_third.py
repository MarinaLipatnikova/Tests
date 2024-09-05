import pytest

from third import vote


@pytest.mark.parametrize(
    'votes, expected',
    (
            [[1,1,1,2,3], 1],
            [[1,2,3,2,2], 2]
    )
)
def test_vote(votes, expected):
    result = vote(votes)
    assert expected == result