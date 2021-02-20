class MinStack:
    """
    设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈
    key: min_stack存储截止当前的最小值
    """

    def __init__(self):
        """
        initialize your data structure here
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]) if self.min_stack else x)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

