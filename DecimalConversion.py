from math import gcd


class DecimalConversion:
    """
    1. Given two integers representing the numerator and denominator of a fraction,
    return the fraction in string format. If the fractional part is repeating,
    enclose the repeating part in parentheses. If multiple answers are possible, return any of them.

    2. Given a decimal number as N, the task is to convert N into an equivalent irreducible fraction.
    An irreducible fraction is a fraction in which numerator and denominator are co-primes i.e.,
    they have no other common divisor other than 1.
    """

    def fractionToDecimal(self,numerator: int,denominator: int) -> str:

        #edge cases
        if denominator == 0:
            return "undefined"
        if numerator == 0:
            return "0"

        #initialize result and check for negative sign
        result = ""
        if (numerator<0)^(denominator<0):
            result += "-"
        numerator, denominator = abs(numerator), abs(denominator)

        #integer part of the result
        result += str(numerator//denominator)

        #check if there is a fractional part
        if numerator%denominator == 0:
            return result

        result += "."

        #use a dictionary to store position of each remainder
        remainder_dict = {}
        remainder = numerator%denominator

        #keep adding remainder to the result until it repeats or remainder becomes 0
        while remainder!=0 and remainder not in remainder_dict:
            remainder_dict[remainder] = len(result)
            remainder *= 10
            result += str(remainder//denominator)
            remainder = remainder%denominator

        #check if there is a repeating part
        if remainder in remainder_dict:
            result = result[:remainder_dict[remainder]] + "(" + result[remainder_dict[remainder]:] + ")"

        return result

    def decimalToFraction(self,num:float) -> str:
        #split the number at decimal and make numerator and denominator to form a fraction
        #now find the highest common divisor among them and return the final answer
        numString = str(num)

        if '.' not in numString:
            return numString

        integerPart, decimalPart = numString.split('.')

        denominator = 10**len(decimalPart)
        numerator = int(integerPart) * denominator + int(decimalPart)

        common_divisor = gcd(numerator,denominator)

        numerator = numerator//common_divisor
        denominator = denominator//common_divisor

        return str(numerator)+"/"+str(denominator)

    def main(self):
        if (self.fractionToDecimal(1,2)=="0.5" and
        self.fractionToDecimal(2,1)=="2" and
        self.fractionToDecimal(4,333)=="0.(012)"):
            print("Pass")
        else:
            print("Fail")

        if (self.decimalToFraction(0.5)=="1/2" and
        self.decimalToFraction(4)=="4" and
        self.decimalToFraction(2.25)=="9/4" and
        self.decimalToFraction(1.75)=="7/4"):
            print("Pass")
        else:
            print("Fail")


conversion = DecimalConversion()
conversion.main()