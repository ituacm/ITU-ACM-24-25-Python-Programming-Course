import math

class Fraction(object):
    """
    a class to represent fractions and perform basic arithmetic operations on them.
    """

    def __init__(self, num, denom):
        """
        initialize a Fraction object with numerator and denominator.
        """
        self.num = num
        self.denom = denom

    def __str__(self):
        """
        return a string representation of the fraction in the form 'numerator/denominator'.
        """
        return f"{self.num}/{self.denom}"

    def simplify(self):
        """
        simplify the fraction by dividing both numerator and denominator by their greatest common divisor (GCD).
        Uses math.gcd to find the GCD.
        """
        gcd = math.gcd(self.num, self.denom)
        self.num //= gcd
        self.denom //= gcd

    def __add__(self, other):
        """
        add two fractions and return the resulting simplified fraction.
        returns Fraction, a new simplified Fraction object as the sum.
        """
        result = Fraction(
            num=(self.num * other.denom + self.denom * other.num),  # calculate the numerator of the sum
            denom=(self.denom * other.denom)  # calculate the common denominator
        )
        result.simplify()  # simplify the resulting fraction
        return result

    def __sub__(self, other):
        """
        subtract one fraction from another and return the result.
        returns Fraction, a new simplified Fraction object as the difference.
        """
        other.num *= -1  # negate the numerator of the second fraction to perform subtraction
        return self + other  # reuse the addition logic for subtraction

    def __mul__(self, other):
        """
        multiply two fractions and return the resulting simplified fraction.
        returns Fraction, a new simplified Fraction object as the product.
        raises TypeError if the `other` object is not a Fraction instance.
        """
        if not isinstance(other, Fraction):
            raise TypeError("operand must be a Fraction instance")  # ensure the operation is between fractions
        num = self.num * other.num  # multiply numerators
        denom = self.denom * other.denom  # multiply denominators
        result = Fraction(num, denom)  # return the resulting fraction
        result.simplify()
        return result

# example usage to test
fraction1 = Fraction(1, 2)  # create a Fraction object representing 1/2
fraction2 = Fraction(2, 3)  # create a Fraction object representing 1/3

print("fraction 1:", fraction1)
print("fraction 2:", fraction2)
print("sum:", fraction1 + fraction2)
print("difference:", fraction1 - fraction2)
print("product:", fraction1 * fraction2)
