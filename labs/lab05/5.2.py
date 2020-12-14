#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import gcd


class Rational:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError(f"denominator is zero")
        elif denominator < 0:
            numerator = -numerator
            denominator = -denominator
        self._numerator = numerator
        self._denominator = denominator
        self.reduce()

    def reduce(self):
        factor = gcd(self._numerator, self._denominator)
        self._numerator //= factor
        self._denominator //= factor

    def __float__(self):
        return self._numerator / self._denominator

    def __neg__(self):
        return Rational(-self._numerator, self._denominator)

    def __add__(self, other):
        if isinstance(other, Rational):
            return_value = Rational(self._numerator * other._denominator + other._numerator * self._denominator,
                                    self._denominator * other._denominator)
        elif isinstance(other, int):
            return_value = Rational(self._numerator + other * self._denominator, self._denominator)
        else:
            return NotImplemented
        return return_value

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, (Rational, int)):
            return self + (-other)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, int):
            return -(self - other)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Rational):
            return_value = Rational(self._numerator * other._numerator, self._denominator * other._denominator)
        elif isinstance(other, int):
            return_value = Rational(self._numerator * other, self._denominator)
        else:
            return NotImplemented
        return_value.reduce()
        return return_value

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return_value = Rational(self._numerator * other._denominator, self._denominator * other._numerator)
        elif isinstance(other, int):
            return_value = Rational(self._numerator, self._denominator * other)
        else:
            return NotImplemented
        return_value.reduce()
        return return_value

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Rational(self._denominator * other, self._numerator)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self._numerator == other._numerator and self._denominator == other._denominator
        elif isinstance(other, int):
            return self._numerator == other and self._denominator == 1
        else:
            return NotImplemented

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"

    @classmethod
    def from_string(cls, string):
        numbers = string.split('/')
        if not len(numbers) == 2:
            raise ValueError(f"{string} cannot be read as rational")
        num = int(numbers[0])
        denom = int(numbers[1])
        if denom <= 0:
            raise ValueError(f"denominator is nonpositive in \"{string}\"")
        return Rational(num, denom)


def test_operations():
    assert Rational(3, 5) + Rational(3, 5) == Rational(6, 5)
    assert Rational(3, 5) + Rational(2, 5) == 1
    assert Rational(3, 5) + 2 == Rational(13, 5)
    assert 7 + Rational(3, 5) == Rational(38, 5)

    assert Rational(4, 7) - 2 == Rational(-10, 7)
    assert 7 - Rational(40, 7) == Rational(9, 7)

    assert Rational(7, 2) * Rational(3, 1) == Rational(21, 2)
    assert Rational(7, 2) * Rational(2, 1) == 7
    assert Rational(7, 2) * 2 == 7
    assert 5 * Rational(3, 25) == Rational(3, 5)
    assert 5 * Rational(3, 30) == Rational(1, 2)
    assert -7 * Rational(-5, -14) == Rational(5, -2)

    assert Rational(5, 7) / Rational(5, 7) == 1
    assert 6 / Rational(12, 5) == Rational(5, 2)

    assert Rational(5, 6) == Rational(5, 6)
    assert Rational(13, 6) == Rational(26, 12)
    assert Rational(36, 6) == 6
    assert Rational(36, 6) != 7
    assert 8 != Rational(4, 6)

    try:
        '4/9' + Rational(5, 9)
    except TypeError as e:
        assert str(e) == "unsupported operand type(s) for +: 'Rational' and 'str'"


def test_cast_to_float():
    assert float(Rational(5, 7)) == 5/7
    assert float(Rational(0, 1)) == 0
    assert float(Rational(42, 10**20)) == 42 / 10**20
    assert float(Rational(12**48, 48)) == 12**48 / 48


def test_parse_from_string():
    assert Rational.from_string("3/3") == 1
    assert Rational.from_string("0/1") == 0
    assert Rational.from_string("-7/6") == Rational(-7, 6)
    assert Rational.from_string("-3512351325/513451345") == Rational(-3512351325, 513451345)

    try:
        Rational.from_string("0/0")
    except ValueError as e:
        assert str(e) == "denominator is nonpositive in \"0/0\""

    try:
        Rational.from_string("7/-6")
    except ValueError as e:
        assert str(e) == "denominator is nonpositive in \"7/-6\""

    try:
        Rational.from_string("4.0/1")
    except ValueError as e:
        assert str(e) == "invalid literal for int() with base 10: '4.0'"


if __name__ == '__main__':
    test_operations()
    test_cast_to_float()
    test_parse_from_string()


# In[ ]:




