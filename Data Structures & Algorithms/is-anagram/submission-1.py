class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for character in s:
            count[character] = count.get(character, 0) + 1

        for character in t:
            if character in count:
                count[character] -= 1
            else:
                return False
        
        for key, value in count.items():
            if value != 0:
                return False
        
        return True
        
        