"""
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps.
    In how many distinct ways can you climb to the top?
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        stepOne, stepTwo = 1,1

        for i in range(0, n-1):
            temp = stepOne
            stepOne = stepOne + stepTwo
            stepTwo = temp
        return stepOne


if __name__ == "__main__":
    #Number of steps
    n = 5
    # Ways to climb the top
    solution = Solution()
    output = solution.climbStairs(n)
    print("Number of ways to climb the stairs: ",output)