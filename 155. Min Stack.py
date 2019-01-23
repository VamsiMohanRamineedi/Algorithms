# Min Stack - Time: O(1), space: O(n)

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.minIndices = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.data:
            self.minIndices.append(0)
        elif self.data[self.minIndices[-1]] >= x:
            self.minIndices.append(len(self.data))
        self.data.append(x)
        return

    def pop(self):
        """
        :rtype: void
        """
        if self.data[self.minIndices[-1]] == self.data[-1]:
            del self.minIndices[-1]
        del self.data[-1]
        return
        

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.data[self.minIndices[-1]]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()