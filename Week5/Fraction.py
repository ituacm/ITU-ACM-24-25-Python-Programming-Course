import math

class Fraction(object):
    def __init__(self,
        num,
        denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return f"{self.num}/{self.denom}"

    def simplify(self):
        gcd = math.gcd(self.num, self.denom)
        self.num //= gcd
        self.denom //= gcd

    def __add__(self, other):
        result = Fraction(
            num=(self.num * other.denom + 
                 self.denom * other.num),
            denom=(self.denom * other.denom)
        )
        result.simplify()
        return result

    def __sub__(self, other):
        other.num *= -1
        return self + other

    def __mul__(self, other):
        pass # TODO - problem set q1