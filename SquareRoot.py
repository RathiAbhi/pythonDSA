class SquareRoot:
    """
    given a number calculate its square root
    using binary search and with a precision upto
    k places
    """

    def squareRoot(self,num:int,k:int):
        ans = 1
        start = 0
        end = num

        while start<=end:
            mid = (start+end)//2
            if mid*mid==num:
                ans = mid
                break

            if mid*mid<num:
                start = mid + 1
                ans = mid
            else:
                end = mid-1

        print(ans)
        increment = 0.1
        for i in range(k):
            while ans*ans<=num:
                ans += increment
            ans -= increment
            increment = increment/10

        print(ans)
        return ans

    def main(self):
        if round(self.squareRoot(50,3),3)==7.071:
            print("pass")
        else:
            print("fail")

root = SquareRoot()
root.main()