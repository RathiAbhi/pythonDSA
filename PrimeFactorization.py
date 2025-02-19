import math


class PrimeFactorization:
    """
    return an array containing prime factorization of a number
    1. An array that contains prime numbers whose product is equal to n
    2. An array that only contains the prime factors
    """
    def primeFactorization(self,n:int)->list[int]:
        primefactors = []
        if n==1:
            return primefactors

        while n%2==0:
            primefactors.append(2)
            n = n/2

        for i in range(3,int(math.sqrt(n)),2):
            while n%i==0:
                primefactors.append(i)
                n = n/i

        if n>2:
            primefactors.append(n)

        return primefactors

    def primeFactors(self,n:int)->list[int]:
        primefactors = []
        if n==1:
            return primefactors

        while n%2==0:
            if 2 not in primefactors:
                primefactors.append(2)
            n = n/2

        for i in range(3,int(math.sqrt(n)),2):
            while n%i==0:
                if i not in primefactors:
                    primefactors.append(i)
                n = n/i

        if n > 2:
            if n not in primefactors:
                primefactors.append(n)
        return primefactors

    def main(self):
        if (self.primeFactorization(315)==[3,3,5,7] and
        self.primeFactorization(24)==[2,2,2,3] and
        self.primeFactorization(6)==[2,3]):
            print("pass")
        else:
            print("wrong factorization")

        if (self.primeFactors(315)==[3,5,7] and
        self.primeFactors(24)==[2,3] and
        self.primeFactors(6)==[2,3]):
            print("pass")
        else:
            print("wrong factors")


prime = PrimeFactorization()
prime.main()