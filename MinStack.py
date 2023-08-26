""" 
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:
    *MinStack() initializes the stack object.
    *void push(int val) pushes the element val onto the stack.
    *void pop() removes the element on the top of the stack.
    *int top() gets the top element of the stack.
    *int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.
    
"""



class MinStack:
    #Define two stacks, one for all the operations mentioned
    # Another for getting the min value
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    # append value into stack 
    # Append value into minStack if it is the current min
    def push(self, val: int) -> None:
        self.stack.append(val)
        # Get the min of the current val and the one in minStack
        # provided minStack is not empty
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        
    # Pop from both stacks since if its removed from the main stack it cannot 
    # be the min value in minStack
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
if __name__ == '__main__' :
    print("LeetCode Problem : 155. Min Stack")
    
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())
