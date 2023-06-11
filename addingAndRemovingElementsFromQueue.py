class MyQueue(object):

    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stk1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.move()
        return self.stk2.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.stk2[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stk1 and not self.stk2
    def move(self):
        if not self.stk2:
            while self.stk1:
                self.stk2.append(self.stk1.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()