import pytest

from second import discriminant, solution


@pytest.mark.parametrize(
    'a, b, c, expected',
    (
        [1, 8 , 15, 4],
        [1, -13, 12, 121],
        [-4, 28, -49, 0],
        [1, 1, 1, -3]
    )
)
def test_discriminant(a, b, c, expected):
    result = discriminant(a, b, c)
    assert expected == result


@pytest.mark.parametrize(
    'a, b, c, expected',
    (
            [1, 8, 15, (-3.0, -5.0)],
            [1, -13, 12, (12.0, 1.0)],
            [-4, 28, -49, 3.5],
            [1, 1, 1, "корней нет"]
    )
)
def test_solution(a, b, c, expected):
    result = solution(a, b, c)
    assert expected == result
