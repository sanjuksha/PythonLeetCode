class Solution:
    def twoSum(self, numbers: list[int], target: int)-> list[int]:
   
        l, r = 0, len(numbers) -1
        
        while l < r:
            currSum = numbers[l] + numbers[r]
            
            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return [l+1, r+1]


if __name__ == "__main__":
    solution = Solution()
    numbers = [2,7,11,15]        
    print("LeetCode Problem 167: Two Sum || - Input Array is sorted")
    result = solution.twoSum(numbers, 9)
    print(result)