class DotProduct:
    def dotProduct(self, arr1: list[int], arr2: list[int]) -> int:
        sum = 0
        for i in range(len(arr1)):
            sum += arr1[i]*arr2[i]

        return sum

    def main(self):
        arr1 = [1,2]
        arr2 = [2,3]
        print(self.dotProduct(arr1,arr2))

product = DotProduct()
product.main()