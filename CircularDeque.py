class CircularDeque:
    def __init__(self, k:int):
        self.queue = [0]*k
        self.front = 0
        self.rear = k-1
        self.size = 0
        self.capacity = k

    def insertFront(self, value:int)->bool:
        if self.isFull():
            return False
        self.front = (self.front-1 + self.capacity)%self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value:int)->bool:
        if self.isFull():
            return False
        self.rear = (self.rear+1)%self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self)->bool:
        if self.isEmpty():
            return False
        self.front = (self.front+1)%self.capacity
        self.size -= 1
        return True

    def deleteLast(self)->bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear-1 + self.capacity)%self.capacity
        self.size -= 1
        return True

    def getFront(self)->int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self)->int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self)->bool:
        return self.size == 0

    def isFull(self)->bool:
        return self.size == self.capacity

obj = CircularDeque(3)
print(obj.insertLast(1))
print(obj.insertLast(2))
print(obj.insertFront(3))
print(obj.insertLast(4))
print(obj.getRear())
print(obj.isFull())
print(obj.deleteLast())
print(obj.insertFront(4))
print(obj.getFront())
print(obj.deleteFront())
print(obj.getFront())
print(obj.isEmpty())
print(obj.deleteFront())
print(obj.deleteFront())
print(obj.isEmpty())