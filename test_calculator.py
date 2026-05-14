"""Unit tests for the calculator module."""

import pytest
from calculator import add, subtract, multiply, divide


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -4) == -5

    def test_mixed_signs(self):
        assert add(-3, 7) == 4

    def test_floats(self):
        assert add(1.5, 2.5) == 4.0

    def test_zero(self):
        assert add(0, 5) == 5


class TestSubtract:
    def test_positive_numbers(self):
        assert subtract(10, 4) == 6

    def test_negative_result(self):
        assert subtract(3, 7) == -4

    def test_zero(self):
        assert subtract(5, 0) == 5

    def test_floats(self):
        assert subtract(3.5, 1.5) == 2.0


class TestMultiply:
    def test_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_negative_numbers(self):
        assert multiply(-2, 5) == -10

    def test_both_negative(self):
        assert multiply(-3, -3) == 9

    def test_zero(self):
        assert multiply(100, 0) == 0

    def test_floats(self):
        assert multiply(2.5, 4) == 10.0


class TestDivide:
    def test_positive_numbers(self):
        assert divide(10, 2) == 5.0

    def test_negative_dividend(self):
        assert divide(-9, 3) == -3.0

    def test_float_result(self):
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_floats(self):
        assert divide(1.5, 0.5) == 3.0
