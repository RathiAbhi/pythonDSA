class HashMap:

    """
    implement a hashmap with insertion and search of O(1) complexity
    without using any in-built library
    """
    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def hash(self,key):
        return key%self.size

    def put(self,key,value):
        index = self.hash(key)
        for pair in self.table[index]:
            #print(f"key = {pair[0]} and value = {pair[1]}")
            if pair[0]==key:
                pair[1] = value
                return

        self.table[index].append([key,value])

    def get(self,key):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0]==key:
                return pair[1]

        return -1

    def remove(self,key):
        index = self.hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0]==key:
                del self.table[index][i]
                return


hashmap = HashMap()
hashmap.put(1,1)
hashmap.put(2,2)
print(hashmap.get(1))
print(hashmap.get(3))
hashmap.put(2,1)
print(hashmap.get(2))
hashmap.remove(2)
print(hashmap.get(2))

