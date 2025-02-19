class PascalTriangle:

    def pascalTriangle(self,col:int,row:int,n:int)->int:
        mat = []

        for i in range(row+1):
            arr = []
            for j in range(i+1):
                if j==0 or j==i:
                    arr.append(1)
                else:
                    arr.append(mat[i-1][j-1]+mat[i-1][j])
            mat.append(arr)

        return mat[row][col]

    def main(self):
        if self.pascalTriangle(1,2, 5)==2:
            print("pass")
        else:
            print("fail")

pascal = PascalTriangle()
pascal.main()