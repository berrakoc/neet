class MinStack:

    def __init__(self):
        # Initialize the main stack and the min stack
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)
        
        # If the min_stack is empty or the current value is smaller than or equal to
        # the top of min_stack, push it onto min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop the value from the main stack
        if self.stack:
            val = self.stack.pop()
            # If the popped value is the same as the top of min_stack, pop from min_stack as well
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        # Return the top element of the min stack, which is the minimum element
        if self.min_stack:
            return self.min_stack[-1]
        return None
