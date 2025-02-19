class CountLengthOfCycle:
    """
    Given an integer array of size n. Elements of the array is >= 0. Starting from arr[startInd],
    follow each element to the index it points to. Find a cycle and return its length.
    No cycle is found -> -1

    Logic: Maintain a dictionary of visited indices
    maintain the index and its position in the visiting sequence
    when we find an already visited index, subtract this index's position
    from total count and return
    """

    def countLengthOfCycleInArray(self, arr: list[int], startIndex: int) -> int:
        print(f"printing the input {arr}")
        if startIndex<0 or startIndex >= len(arr):
            return -1

        visited = {}
        count = 1

        while True:
            if startIndex >= len(arr) or startIndex<0:
                return -1

            if startIndex in visited:
                return count - visited[startIndex]

            visited[startIndex] = count
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

"""
more optimum solution could have been the fast and slow pointer
cycle detection. And for length, stop one, and when the other again
comes, count that as the length of the cycle
"""