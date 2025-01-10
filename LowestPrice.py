class LowestPrice:
    """
    find out the lowest price for an item
    at any time during the day
    """
    def lowestPrice(self, val: list[list[int]])-> list[list[int]]:
        ans = []
        store = {}
        for i in range(len(val)):
            startTime = val[i][0]
            endTime = val[i][1]
            price = val[i][2]

            for j in range(startTime,endTime+1):
                num = store.get(j,0)
                if num==0:
                    store[j] = price
                elif price < store[j]:
                    store[j] = price

        start_key = None
        current_value = None
        for key in sorted(store):
            if current_value is None or store[key]!=current_value:
                if current_value is not None:
                    ans.append([start_key, key-1, current_value])
                start_key = key
                current_value = store[key]

        ans.append([start_key, key, current_value])

        return ans

    def main(self):
        arr = [[1,5,20],[3,8,15],[7,10,8]]
        if self.lowestPrice(arr)==[[1,2,20],[3,6,15],[7,10,8]]:
            print("pass")
        else:
            print("fail")

price = LowestPrice()
price.main()