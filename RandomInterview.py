"""
given an integer n, find the number of trailing zeroes in n factorial
sum of all the multiples of 3 and 5 below n
sort array of 0,1,2 without sorting - nust count their number and assign accordingly
"""
class RandomInterview:
    def TrailingZeroes(self,n):
        count = 0
        while n>1:
            n = n//5
            count += n

        return count

    def SumOfMultiplesOf3And5(self,n):
        q1,q2,q3 = n//3,n//5,n//15
        s1 = 3*(q1*(q1+1))/2
        s2 = 5*(q2*(q2+1))/2
        s3 = 15*(q3*(q3+1))/2
        s = s1+s2-s3

        return s



    def main(self):
        print(self.TrailingZeroes(90))
        print(self.SumOfMultiplesOf3And5(20))

random = RandomInterview()
random.main()