
class BishopMoves:
    """
    1. Min number of steps required for a bishop to reach a position if start is given
    2. Total number of squares visited by a bishop in one move

    Logic: The bishop can only move diagonally, however there is no limit on the number of
    steps that it can take. So, if the end position is on the same diagonal line to the start
    position, then the bishop will take only 1 step. Also one more thing to note here is that
    bishop can only move to the same color, if it starts on white it can reach to only white. Hence,
    if start and end are on different colors then we return -1 (i.e. impossible). Eevrything else
    can be done in 2 moves.
    Same color logic: squares of same color on horizontal and vertical lines are at a difference of
    2 from the given starting position, and diagonally both x and y would be at a difference of 1.
    Hence, whatever the remainder for 2 is at the start position, would be same throughout all the
    squares of that very same color.

    For total squares to be covered by bishop we just see the total moves it can make in 4 diagonal
    directions before hitting the edges. The position is given as (row,col) from 1 to 8
    """

    def minMoves(self, start: list[int], end: list[int]) -> int:
        x_start = start[0]
        y_start = start[1]
        x_end = end[0]
        y_end = end[1]

        if x_start == x_end and y_start == y_end:
            return 0
        elif abs(x_end-x_start) == abs(y_end-y_start):
            return 1
        elif (x_start % 2 == y_start % 2) != (x_end % 2 == y_end % 2):
            return -1
        else:
            return 2

    def totalMoves(self, start: list[int]) -> int:
        row = start[0]
        col = start[1]

        topLeft = min(row-1, col-1)
        topRight = min(row-1, 8-col)
        bottomLeft = min(8-row, col-1)
        bottomRight = min(8-row, 8-col)

        return topLeft+topRight+bottomRight+bottomLeft
    def main(self):
        # row, col are given as position
        start = [0,0]
        end = [6,0]
        pos = [4,4]
        print(self.minMoves(start,end))
        print(self.totalMoves(pos))

moves = BishopMoves()
moves.main()