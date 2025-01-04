class CountLengthOfCycle:
    """
    Given an integer array of size n. Elements of the array is >= 0. Starting from arr[startInd],
    follow each element to the index it points to. Find a cycle and return its length.
    No cycle is found -> -1

    Logic: Maintain a set of visited indices, and keep pushing each index to set and in case there
    is a repetition of indices, return the size of count as the length of cycle
    """

    def countLengthOfCycleInArray(self, arr: list[int], startIndex: int) -> int:
        print(f"printing the input {arr}")
        if startIndex<0 or startIndex >= len(arr):
            return -1

        visited = set()
        count = 0

        while True:
            if startIndex >= len(arr):
                return -1

            if arr[startIndex] in visited:
                return count

            visited.add(arr[startIndex])
            count += 1
            startIndex = arr[startIndex]


    def main(self):
        if (self.countLengthOfCycleInArray([1,2,0],0)==3 and
        self.countLengthOfCycleInArray([1,0],0)==2 and
        self.countLengthOfCycleInArray([1,2,3,1], 0) == 3 and
        self.countLengthOfCycleInArray([1,2,3,4], 0) == -1 and
        self.countLengthOfCycleInArray([1,2,3,4], -1) == -1 and
        self.countLengthOfCycleInArray([1,2,3,4], 4) == -1 and
        self.countLengthOfCycleInArray([2,3,4,0], 0) == -1 and
        self.countLengthOfCycleInArray([2,3,0], 0) == 2):
            print("Pass")
        else:
            print("fail")


count = CountLengthOfCycle()
count.main()