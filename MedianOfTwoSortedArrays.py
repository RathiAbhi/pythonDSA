class MedianArrays:
    # Python Program to find the median of two sorted arrays
    # of different size using Binary Search

    def medianOf2(self,a, b):
        n = len(a)
        m = len(b)

        # If a[] has more elements, then call medianOf2
        # with reversed parameters
        if n > m:
            return self.medianOf2(b, a)

        lo = 0
        hi = n
        while lo <= hi:
            mid1 = (lo + hi) // 2
            mid2 = (n + m + 1) // 2 - mid1

            # Find elements to the left and right of partition in a[]
            l1 = (mid1 == 0) and float('-inf') or a[mid1 - 1]
            r1 = (mid1 == n) and float('inf') or a[mid1]

            # Find elements to the left and right of partition in b[]
            l2 = (mid2 == 0) and float('-inf') or b[mid2 - 1]
            r2 = (mid2 == m) and float('inf') or b[mid2]

            # If it is a valid partition
            if l1 <= r2 and l2 <= r1:

                # If the total elements are even, then median is
                # the average of two middle elements
                if (n + m) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0

                # If the total elements are odd, then median is
                # the middle element
                else:
                    return max(l1, l2)

            # Check if we need to take lesser elements from a[]
            if l1 > r2:
                hi = mid1 - 1

            # Check if we need to take more elements from a[]
            else:
                lo = mid1 + 1
        return 0


    def main(self):
        a = [1, 12, 15, 26, 38]
        b = [2, 13, 17, 30, 45, 60]

        print(self.medianOf2(a, b))

median = MedianArrays()
median.main()