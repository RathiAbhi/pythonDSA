class StairCase:
    """
    There is a staircase with 'n' number of steps. A child
    walks by and wants to climb up the stairs, starting at
    the bottom step and ascending to the top. Instead
    of taking 1 step at a time, it will vary between taking
    either 1, 2 or 3 steps at a time.
    Given 'n' number of steps below method should find
    number of
    unique combinations the child could traverse.
    An example would be countSteps(3) == 4:
    1 1 1
    2 1
    1 2
    3

    Logic: use dynamic programming which counts
    the combination to reach each step is the sum
    of combinations of all the prior steps
    """

    def stairs(self,n:int)->int:
        if n==0 or n==1:
            return 1

        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        #print(dp)
        return dp[n]

    def main(self):
        if (self.stairs(3)==4 and
        self.stairs(4)==7 and
        self.stairs(5)==13):
            print("pass")
        else:
            print("fail")

stair = StairCase()
stair.main()