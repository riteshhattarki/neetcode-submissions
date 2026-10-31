class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstString = sorted(s)
        secondString = sorted(t)
        return firstString == secondString

        