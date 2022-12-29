import pytest
from flatten import flatten

@pytest.mark.parametrize("input, output", [
    ([], []),
    ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([1, [2, [3, [4, 5]]]], [1, 2, 3, 4, 5]),
    ([[1, [2, [3, [4, 5, 6]]]]], [1, 2, 3, 4, 5, 6]),
    ([[1, 2, 3, [4, 5, [6]]]], [1, 2, 3, 4, 5, 6]),
    ([[[[6]]]], [6]),
    ])
def test_flatten(input, output):

    assert flatten(input, []) == output