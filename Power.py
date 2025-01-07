class Power:
    def powerCompute(self, base:int, exponent:int)->float:
        if exponent==0:
            return 1
        elif exponent==1:
            return base

        absExponent = abs(exponent)
        product = base
        for i in range(2,absExponent+1):
            product *= base

        if exponent<0:
            return 1/product
        else:
            return product

    def main(self):
        if self.powerCompute(2,6)==64 and self.powerCompute(2,-4)==0.0625:
            print("Pass")
        else:
            print("Fail")

compute = Power()
compute.main()