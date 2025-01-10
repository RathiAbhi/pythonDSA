import sys

class SecondSmallest:
    """
    given an array, return the second smallest element
    [4,3,1,1] should return 1 not 3
    """

    def secondSmallest(self,arr:list[int])->int:
        if len(arr)<2:
            return 0

        firstMin = sys.maxsize
        secondMin = sys.maxsize

        for i in arr:
            if i<firstMin:
                secondMin = firstMin
                firstMin = i
            elif i<secondMin:
                secondMin = i

        return secondMin

    def main(self):
        if (self.secondSmallest([4,8,9,2,1,1])==1 and
        self.secondSmallest([3,4,5,6,1,2])==2):
            print("pass")
        else:
            print("fail")

small = SecondSmallest()
small.main()