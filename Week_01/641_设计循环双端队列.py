class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.q = [0 for _ in range(k)]
        self.head = 1
        self.tail = 0
        self.head2tail = 1  # 为1时代表head在tail前面，为0时代表tail在head前面

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.head == 0:
            self.head = len(self.q)
            self.head2tail = 1 - self.head2tail
        self.head -= 1
        self.q[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.tail == len(self.q) - 1:
            self.tail = -1
            self.head2tail = 1 - self.head2tail
        self.tail += 1
        self.q[self.tail] = value
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self.head == len(self.q) - 1:
            self.head = -1
            self.head2tail = 1 - self.head2tail
        self.head += 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self.tail == 0:
            self.tail = len(self.q)
            self.head2tail = 1 - self.head2tail
        self.tail -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.q[self.head]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.q[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if (self.tail + 1 == self.head and self.head2tail) or (self.head == 0 and self.tail == len(self.q) - 1 and not self.head2tail):
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if (self.tail + 1 == self.head and not self.head2tail) or (self.head == 0 and self.tail == len(self.q) - 1 and self.head2tail):
            return True
        else:
            return False