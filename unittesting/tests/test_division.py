from unittesting.my_funcs.utils import division
import pytest

@pytest.mark.parametrize('a, b, expected_result', [(10, 2, 5),
                                                   (10, 5, 2),
                                                   (30, -3, -10),
                                                   (4, 2, 2),
                                                   (40, 20, 2)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result

# def test_division_one():
#     assert division(10, 5) == 2

@pytest.mark.parametrize('expected_exeption, divider, divisionable', [(ZeroDivisionError, 0, 10), (TypeError, '2', 20)])
def test_errors_division(expected_exeption, divider, divisionable):
    # контекстный менеджер
    with pytest.raises(expected_exeption):
        division(divisionable, divider)
