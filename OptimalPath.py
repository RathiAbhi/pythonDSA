class OptimalPath:
    """
    you have to collect rocks in a grid
    starting from the bottom left corner and have to reach top right corner
    """
    def optimalPath(self,grid: list[list[int]])->int:
        rows, cols = len(grid),len(grid[0])
        result = [[0 for i in range(cols)] for i in range(rows)]

        #making a 2d dp array, seeking the possibility of arriving
        #at that position

        result[rows-1][0] = grid[rows-1][0]
        for i in range(rows-2,-1,-1):
            #filling the first column
            result[i][0] = result[i+1][0] + grid[i][0]

        for i in range(1,cols):
            #filling the last row
            result[rows-1][i] = result[rows-1][i-1] + grid[rows-1][i]

        for i in range(rows-2,-1,-1):
            for j in range(1,cols):
                result[i][j] = grid[i][j] + max(result[i+1][j],result[i][j-1])

        return result[0][cols-1]

    def main(self):
        if (self.optimalPath([[0,0,0,0,5],[0,1,1,1,0],[2,0,0,0,0]])==10 and
        self.optimalPath([[1,3,2,0,2,1,8],[3,4,1,2,0,1,1],[1,1,1,2,3,2,1],[1,0,1,1,4,2,1]])==25):
            print("pass")
        else:
            print("fail")

path = OptimalPath()
path.main()