class Powerof10:
    """
    given an integer, return true if it's a power of 10
    """

    def powerTen(self, n:int)-> bool:
        if n==1:
            return True

        while n>1 and n%10==0:
            n = n/10

        return n==1

    def main(self):
        if self.powerTen(1000) and not self.powerTen(85):
            print("pass")
        else:
            print("fail")


power = Powerof10()
power.main()