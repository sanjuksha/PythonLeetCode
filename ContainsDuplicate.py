
class Solution(object):
    """
        This function returns true if any value appears
        at least twice in the array, and return false
        if every element is distinct.
    """
    def containsDuplicate(self, nums):
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False



if __name__ == '__main__':
    print("LeetCode Problem: 217. Contains Duplicate")
    nums = [1,1,1,3,3,4,3,2,4,2]

    solution = Solution()
    result = solution.containsDuplicate(nums)
    print(result)