"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    
Returns:
    bool : true if paranthesis are valid, false otherwise.
"""


class Solution(object):
    def isValid(self, s:str)-> bool:
        stack = []
        closeToOpen = {")":"(", "}" : "{", "]": "["}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False
        
if __name__ == '__main__' :
    print("LeetCode Problem: 20. Valid Parantheses")
    s = "[(){}]"
    solution = Solution()
    result = solution.isValid(s)
    print(result)
    
    