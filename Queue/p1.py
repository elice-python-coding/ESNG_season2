class MyCircularQueue:

    def __init__(self, k: int):
        self.cq = [None] * k
        self.rear = 0
        self.front = 0

    # rear 포인터 이동
    def enQueue(self, value: int) -> bool:

        if self.rear < len(self.cq):
            print(len(self.cq))
            self.cq[self.rear] = value
            self.rear += 1
            return True
        elif self.rear == len(self.cq):
            return False

    def deQueue(self) -> bool:
        if self.rear == 0:
            return False
        else:
            self.cq.pop()
            self.rear -= 1
            return True

    def Front(self) -> int:
        return self.cq[self.front]

    def Rear(self) -> int:
        if self.rear <= len(self.cq):
            return self.cq[self.rear - 1]
        else:
            return False

    def isEmpty(self) -> bool:
        return self.cq[0] == None

    def isFull(self) -> bool:
        return self.rear == len(self.cq)

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()