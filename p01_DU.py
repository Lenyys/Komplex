
import math


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self._imag >= 0:
            return f"{self._real} + {self._imag}i"
        else:
            return f"{self._real} - {abs(self._imag)}i"

    def __repr__(self):
        return f"ComplexNumber({self._real}, {self._imag})"

    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self._real == other and self._imag == 0
        if self._real == other.real and self._imag == other.imag:
            return True
        return False

    def absolute_value(self):
        abs_value = math.sqrt(self._real**2 + self._imag**2)
        return abs_value

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.absolute_value() < ComplexNumber(other, 0).absolute_value()
        if self.absolute_value() < other.absolute_value():
            return True
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.absolute_value() > ComplexNumber(other, 0).absolute_value()
        if self.absolute_value() > other.absolute_value():
            return True
        return False

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, num):
        if isinstance(num, int) or isinstance(num, float):
            self._real = num
        else:
            raise ValueError

    @property
    def imag(self):
        return self._imag

    @imag.setter
    def imag(self, num):
        if isinstance(num, int) or isinstance(num, float):
            self._imag = num
        else:
            raise ValueError

    def add(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ComplexNumber(self._real + other, self._imag)
        real_result = self._real + other.real
        imag_result = self._imag + other.imag
        return ComplexNumber(real_result, imag_result)

    def subtract(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ComplexNumber(self._real - other, self._imag)
        real_result = self._real - other.real
        imag_result = self._imag - other.imag
        return ComplexNumber(real_result, imag_result)

    def multiply(self, other):
        if isinstance(other, int) or isinstance(other, float):
            real_result = (self._real * other)
            imag_result = (self._imag * other)
            return ComplexNumber(real_result, imag_result)
        real_result = (self._real * other.real) - (self._imag * other.imag)
        imag_result = (self._real * other.imag) + (self._imag * other.real)
        return ComplexNumber(real_result, imag_result)

    def divide(self, other):
        if isinstance(other, int) or isinstance(other, float):
            if other == 0:
                raise ZeroDivisionError
            real_result = self._real / other
            imag_result = self.imag / other
            return ComplexNumber(real_result, imag_result)
        denominator = other.real**2 + other.imag**2
        if denominator == 0:
            raise ZeroDivisionError
        real_result = (self._real * other.real + self._imag * other.imag) / denominator
        imag_result = (self._imag * other.real - self._real * other.imag) / denominator
        return ComplexNumber(real_result, imag_result)

    def conjugate(self):
        return ComplexNumber(self._real, -self._imag)


if __name__ == "__main__":
    komplex = ComplexNumber(4, 9)
    print(komplex)
