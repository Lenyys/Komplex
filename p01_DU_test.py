
import pytest
from p01_DU import ComplexNumber


class Test:

    def test_str(self):
        assert str(ComplexNumber(2, 4)) == "2 + 4i"
        assert str(ComplexNumber(-3, -5)) == "-3 - 5i"
        assert str(ComplexNumber(-5, 3)) == "-5 + 3i"
        assert str(ComplexNumber(4, -6)) == "4 - 6i"

    def test_init_setter(self):
        with pytest.raises(ValueError):
            assert ComplexNumber("ctyri", 9)
            assert ComplexNumber(4, "9")

    def test_repr(self):
        assert repr(ComplexNumber(2, 4)) == "ComplexNumber(2, 4)"
        assert repr(ComplexNumber(-3, -5)) == "ComplexNumber(-3, -5)"
        assert repr(ComplexNumber(-5, 3)) == "ComplexNumber(-5, 3)"
        assert repr(ComplexNumber(4, -6)) == "ComplexNumber(4, -6)"

    def test_lt(self):
        assert (ComplexNumber(2, 4) < ComplexNumber(3, 5)) is True
        assert (ComplexNumber(3, 5) < ComplexNumber(2, 4)) is False
        assert (ComplexNumber(2, -4) < ComplexNumber(5, -3)) is True
        assert (ComplexNumber(3, -5) < ComplexNumber(-2, 4)) is False
        assert (ComplexNumber(3, -5) < 5) is False
        assert (ComplexNumber(3, -5) < 2.5) is False
        assert (ComplexNumber(3, -5) < 12.5) is True
        assert (ComplexNumber(3, -5) < 10) is True

    def test_gt(self):
        assert (ComplexNumber(2, 4) > ComplexNumber(1, 3)) is True
        assert (ComplexNumber(3, 5) > ComplexNumber(6, 14)) is False
        assert (ComplexNumber(2, -4) > ComplexNumber(1, -5)) is False
        assert (ComplexNumber(3, -5) > ComplexNumber(-2, 4)) is True
        assert (2.5 < ComplexNumber(3, -5)) is True
        assert (5 < ComplexNumber(3, -5)) is True
        assert (10 < ComplexNumber(3, -5) ) is False
        assert (10.3 < ComplexNumber(3, -5)) is False

    def test_addition(self):
        assert ComplexNumber(2, 4).add(ComplexNumber(1, 3)) == ComplexNumber(3, 7)
        assert ComplexNumber(2, 4).add(ComplexNumber(-1, -3)) == ComplexNumber(1, 1)
        assert ComplexNumber(2, 4).add(ComplexNumber(1, -3)) == ComplexNumber(3, 1)
        assert ComplexNumber(2, 4).add(ComplexNumber(0, 3)) == ComplexNumber(2, 7)
        assert ComplexNumber(2, 4).add(2) == ComplexNumber(4, 4)
        assert ComplexNumber(2, 4).add(2.5) == ComplexNumber(4.5, 4)

    def test_eq(self):
        assert (ComplexNumber(2, 4) == ComplexNumber(2, 4)) is True
        assert (ComplexNumber(3, 5) == ComplexNumber(6, 14)) is False
        assert (ComplexNumber(2, -4) == ComplexNumber(1, -5)) is False
        assert (ComplexNumber(3, -5) == ComplexNumber(3, -5)) is True
        assert (ComplexNumber(3, 0) == 3) is True
        assert (ComplexNumber(3.4, 0) == 3.4) is True
        assert (ComplexNumber(3, 0) == 3.4) is False
        assert (ComplexNumber(3.4, 6) == 3.4) is False

    def test_absolute_value(self):
        assert ComplexNumber(0, 5).absolute_value() == 5
        assert ComplexNumber(-6, 0).absolute_value() == 6


    def test_subtraction(self):
        assert ComplexNumber(2, 4).subtract(ComplexNumber(1, 3)) == ComplexNumber(1, 1)
        assert ComplexNumber(2, 4).subtract(ComplexNumber(-1, -3)) == ComplexNumber(3, 7)
        assert ComplexNumber(2, 4).subtract(ComplexNumber(1, -3)) == ComplexNumber(1, 7)
        assert ComplexNumber(2, 4).subtract(ComplexNumber(0, 3)) == ComplexNumber(2, 1)
        assert ComplexNumber(2, 4).subtract(4) == ComplexNumber(-2, 4)
        assert ComplexNumber(2, 4).subtract(2.5) == ComplexNumber(-0.5, 4)

    def test_multiply(self):
        assert ComplexNumber(2, 4).multiply(ComplexNumber(1, 3)) == ComplexNumber(-10, 10)
        assert ComplexNumber(2, 4).multiply(ComplexNumber(-1, -3)) == ComplexNumber(10, -10)
        assert ComplexNumber(2, 4).multiply(4) == ComplexNumber(8, 16)
        assert ComplexNumber(2,4).multiply(2.5) == ComplexNumber(5, 10)

    def test_conjugate(self):
        assert ComplexNumber(2, 4).conjugate() == ComplexNumber(2, -4)
        assert ComplexNumber(0, 4).conjugate() == ComplexNumber(0, -4)
        assert ComplexNumber(-3, -4).conjugate() == ComplexNumber(-3, 4)

    def test_division(self):
        assert ComplexNumber(2, 4).divide(ComplexNumber(0, 4)) == ComplexNumber(1, -0.5)
        assert ComplexNumber(8, 4).divide(2) == ComplexNumber(4, 2)
        assert ComplexNumber(10, 5).divide(2.5) == ComplexNumber(4, 2)
