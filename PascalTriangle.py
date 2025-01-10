class PascalTriangle:

    def pascalTriangle(self,col:int,row:int,n:int)->int:
        mat = []

        for i in range(n):
            arr = []
            for j in range(i+1):
                if i==j or j==0:
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