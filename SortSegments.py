class SortSegments:
    """
    Given a jumbled collection of segments, each of which is represented as a
    Pair(startPoint, endPoint), this function sorts the segments to make a continuous path.
    A few assumptions you can make:
    1. Each particular segment goes in one direction only,
    i.e.: if you see (1, 2), you will not see (2, 1).
    2. Each starting point only have one way to the end point,
    i.e.: if you see (6, 5), you will not see (6, 10), (6, 3), etc.

    For example, if you're passed a list containing the following int arrays:
    [(4, 5), (9, 4), (5, 1), (11, 9)]

    Then your implementation should sort it such:
    [(11, 9), (9, 4), (4, 5), (5, 1)]

    Logic:
    1. map the start->end so that it becomes easier to find the next segment
    2. in order to start, look for the segment whose start is not an end to any other segment
    because that is how it would not be linked to any other segment
    and becomes the starting point of our new continuous path
    """

    def sortSegments(self,segment:list[list[int]])->list[list[int]]:
        segmentMap = {start:end for start,end in segment}

        all_starts = set(segmentMap.keys())
        all_ends = set(segmentMap.values())

        start = (all_starts - all_ends).pop()

        sortedPath = []
        while start in segmentMap:
            end = segmentMap[start]
            sortedPath.append([start,end])
            start = end

        return sortedPath

    def main(self):
        if self.sortSegments([[4,5],[11,9],[9,4],[5,6],[6,1]])==[[11,9],[9,4],[4,5],[5,6],[6,1]]:
            print("pass")
        else:
            print("fail")

segment = SortSegments()
segment.main()