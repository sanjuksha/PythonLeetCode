class Solution(object):
    def twoSum(self, nums, target):
        #Creating a hash map of val : index
        prevMap = {}

        for i , n, in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return


if __name__ == '__main__' :
    print("LeetCode Problem: 1. Two Sum")
    nums = [3,2,4]
    target = 6
    solution = Solution()
    a,b = solution.twoSum(nums, target)
    print("Output: [",a, "," ,b, "]")