import sys


class SnowPack:
    """
    similar to trapping rain water
    given an array of height of blocks, find out how much snow can be hold between blocks
    logic: maintain leftMax and rightMax array
    at any point, snow = min(leftMax[i],rightMax[i[) - height[i]
    """
    def snowPack(self,heights:list[int])->int:
        leftMax = [0 for i in range(len(heights))]
        rightMax = [0 for i in range(len(heights))]
        n = len(heights)
        leftMax[0] = 0
        for i in range(1,n):
            leftMax[i] = max(heights[i],leftMax[i-1])

        rightMax[n-1] = heights[n-1]
        for i in range(n-2,-1,-1):
            rightMax[i] = max(heights[i],rightMax[i+1])

        snow = 0
        for i in range(n):
            snow += min(leftMax[i],rightMax[i]) - heights[i]

        print(snow)
        return snow

    def main(self):
        if self.snowPack([0,1,3,0,1,2,0,4,2,0,3,0])==13:
            print("pass")
        else:
            print("fail")

snow = SnowPack()
snow.main()