import sys


class Test:

    def test(self,n,sprints):
        vis = {}
        for i in range(len(sprints)-1):
            start = sprints[i]
            end = sprints[i+1]
            if start>end:
                while start > end:
                    vis[start] = vis.get(start,0)+1
                    start -= 1
            else:
                while start <= end:
                    vis[start] = vis.get(start,0)+1
                    start -= 1

        print(vis)

        maxVal = -sys.maxsize
        maxKey = sys.maxsize
        for key,val in vis.items():
            if val > maxVal:
                if key < maxKey:
                    maxKey = key
                    maxVal = val

        return maxKey

    def main(self):
        sprints = [2,4,1,3]
        n = 5
        key = self.test(n,sprints)
        print(key)

r = Test()
r.main()

"""
[3, 5, 6, 1, 7, 8] -> [8 3 5 6 1 7] -> []


newIndex = (index + k)%(len(arr))


n = 1

if (n%4)==1: -> rightward, n += 1, constraint: row=0, col= n-1
elif (n%4)==2: -> move down
elif (n%4)==3: -> left
else: up

[1   2  3   10
4   5   6   11
7   8   9   12
13  14  15  16]

ans = []
rows,cols = n-1,n-1
i = 1
j,k = 0,0
while True:
  if i%4==1:
    while(j<=cols):
      ans.append(mat[k][j])
      j += 1
    k += 1
    cols -= 1
    rows -= 1

  elif i%4==2:
    while(k<=rows):
    rows -= 

  i += 1
  cols -= 1

  if len(arr)==(n-1*n-1):
    break


[4, 1, 5, 2] -> [5 2 5 3] -> [5 3 6 4] -> [6 4 6 5] -> [6 5 7 6] -> [7 6 7 7] -> [7 7 8 8] -> [8 8 8 9] -> [9 9 9 9]

 pick the max element
 calculate the difference a[i] - max where i!=max
 sum all the differences

 P(H)=2/3, P(T)=1/3, 5 times, E(no. of heads)
 X = no of heads, x1, x2, x3, x4, x5, x0
 P(X) = 2/3

 E(X) = p1x1 + p2x2 + ..... = (1/3)^5[1*2 + (nC2)2^2 + (nC3)2^3+ ......]
"""