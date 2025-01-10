class TrappingRainWater:
    """
    similar to leetcode trapping rain water
    """

    def trappingWater(self,heights:list[int])->int:
        n = len(heights)
        leftMax = [0 for i in range(n)]
        rightMax = [0 for i in range(n)]

        leftMax[0] = 0
        for i in range(1,n):
            leftMax[i] = max(heights[i],leftMax[i-1])

        rightMax[n-1] = heights[n-1]
        for i in range(n-2,-1,-1):
            rightMax[i] = max(heights[i],rightMax[i+1])

        water = 0
        for i in range(n):
            water += min(leftMax[i],rightMax[i]) - heights[i]

        return water

    def main(self):
        if self.trappingWater([0,1,0,2,1,0,1,3,2,1,2,1])==6:
            print("pass")
        else:
            print("fail")

water = TrappingRainWater()
water.main()