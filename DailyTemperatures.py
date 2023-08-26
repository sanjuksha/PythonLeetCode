"""Given an array of integers temperatures represents the daily temperatures,
   return an array answer such that answer[i] is the number of days you have to
   wait after the ith day to get a warmer temperature. If there is no future day for 
   which this is possible, keep answer[i] == 0 instead.

   Returns:
    list : days to wait for a warmer temperature
"""



class Solution:
    def dailyTemperatures(sefl, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = [] # A stack of pairs (index, temperatures)
        
        for ind , temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackInd, stackT = stack.pop()
                answer[stackInd] = (ind - stackInd)
            stack.append([ind, temp])
        return answer

if __name__ == '__main__':
    print("LeetCode Problem 739: Daily Temperatures")
    temperatures = [73,74,75,71,69,72,76,73]
    print("Temperatures = ",temperatures)
    solution = Solution()
    answer = solution.dailyTemperatures(temperatures)
    print(answer)