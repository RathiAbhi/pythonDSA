import sys

class LowestPrice:
    """
    Find out the lowest price for an item at any time during the day.
    """
    def lowestPrice(self, val: list[list[int]]) -> list[list[int]]:
        price_map = {}

        for info in val:
            start,end,price = info
            for time in range(start,end+1):
                if time in price_map:
                    if price_map[time]>price:
                        price_map[time] = price
                else:
                    price_map[time] = price

        if not price_map:
            return []

        result = []
        sorted_times = sorted(price_map.keys())
        start_time = sorted_times[0]
        current_price = price_map[start_time]

        for time in sorted_times[1:]:
            if price_map[time]==current_price:
                continue
            else:
                result.append([start_time,time,current_price])
                start_time = time
                current_price = price_map[time]

        result.append([start_time,sorted_times[-1],current_price])
        print(result)
        return result


    def main(self):
        arr = [[1, 5, 20], [3,8,15], [7, 10, 8]]
        expected_result = [[1, 2, 20], [3, 6, 15], [7, 10, 8]]

        if self.lowestPrice(arr) == expected_result:
            print("pass")
        else:
            print("fail")

# Test
price = LowestPrice()
price.main()