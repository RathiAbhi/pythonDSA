class SmallestNumber:
    """
    given a sorted rotated array
    we need to find the min element in O(logN)
    """
    def smallest(self,arr:list[int])->int:
        n = len(arr)
        start,end = 0,n-1

        while start<end:
            if arr[start]<arr[end]:
                return arr[start]

            mid = (start+end)//2
            if arr[mid]>arr[end]:
                start = mid + 1
            else:
                end = mid

        return arr[start]

    def main(self):
        if (self.smallest([3,4,5,6,1,2])==1 and
        self.smallest([5,6,1,2,3,4])==1 and
        self.smallest([2,3])==2):
            print("pass")
        else:
            print("fail")

number = SmallestNumber()
number.main()