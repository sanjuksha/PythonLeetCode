"""
    Given two strings s and t,
    return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the
    letters of a different word or phrase, typically using
    all the original letters exactly once.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Create two hash maps
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

if __name__ =="__main__":
    s = "anagram"
    t = "nagaram"
    print("LeetCode Problem 242: Valid Anagram")
    solution = Solution()
    result = solution.isAnagram(s,t)
    print(result)

# Another Solution
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
"""