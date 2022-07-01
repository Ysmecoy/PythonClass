from fractions import gcd

from math import fabs
class Fraction:
    #constructor
    def __init__(self, numerator = 0, denominator = 1):
        """Construct a Fraction Object.
        :param numerator: numerator of the fraction
        :type numerator: int
        :param denominator: denominator of the fraction
        :type denominator: int
        :rtype: None
        """
        #data field
        self._numerator, self._denominator = numerator, denominator
        self._reduce() # reduce the fraction into irreducible form
        
        
    #Getters
    def get_numerator(self):
        """Returns the numerator of the fraction.
        returns: numerator of the fraction
        :rtype: int
        """
        return self.numerator 
        
    def get_denominator(self):
        """Returns the denominator of the fraction.
        returns: denominator of the fraction
        :rtype: int
        """
        return self.denominator 
    
    # Setters
    def set_numerator(self, numerator):
        """Update the numerator of the fraction.
        returns: updated value of the numerator of the fraction
        :type numerator: int
        :rtype: None
        """
        self._numerator = numerator
        self._reduce()
        
    def set_denominator(self, denominator):
        """Update the denominator of the fraction.
        returns: updated value of the denominator of the fraction
        :type denominator: int
        :rtype: None
        """
        self._denominator = denominator
        self._reduce()  
        
    # Methods  
    #algorithm to find the GCD of two positive integers
    def _gcd(self, x, y):
        """Finds the greatest common divisor of two positive integers.
        :param x: first positive integer
        :type x: int
        :param y: second positive integer
        :type y: int
        returns: greatest common divisor of the two integers
        :rtype: int
        """
        if x < y: return self._gcd(y,x)
        if x % y == 0: return y
        return self._gcd(y, x % y) 
    
    def _reduce(self):
        if self._numerator == 0: self._denominator = 1
        else:
            gcd = self._gcd(round(fabs(self._numerator)), self._denominator)
            self._numerator //= gcd
            self._denominator //= gcd
    def __str__(self):
        """Customizes the output format of the fraction.
        :returns: a string representing the output format of the fraction
        :rtype: str
        """
        return "%d/%d" %(self._numerator, self._denominator)
    
    def _opposite(self):
        """Returns the opposite of the fraction.
        :returns: opposite of the fraction
        :rtype: Fraction
        """
        return Fraction(-self._numerator, self._denominator)
    def _reciprocal(self):
        """Returns the reciprocal of the fraction.
        :returns: reciprocal of the fraction
        :rtype: Fraction
        """
        sign = 1 if self._numerator > 0 else -1
        result = Fraction()
        result._numerator = sign*self._denominator
        result._denominator = round(fabs(self._numerator))
        return result

    #overloading operators
    def __add__(self, other):
        """Adds the fraction with another fraction or integer using operator '+'.
        :param other: another fraction or integer to add to the current fraction
        :type other: Fraction or int
        :returns: addition result
        :rtype: Fraction
        """
        if isinstance(other, int):
            other = Fraction(other,1) #convert the integer to a fraction.
        result = Fraction()
        result._numerator = self._numerator*other._denominator + self._denominator*other._numerator
        result.denominator = self._denominator* other._denominator
        result.reduce()
        return result
    