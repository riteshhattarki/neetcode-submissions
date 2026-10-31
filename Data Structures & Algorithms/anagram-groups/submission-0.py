class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        words = {}
        for str in strs:
            sortedList = []
            sortedList = sorted(str)
            sortedString = "".join(sortedList)
            if sortedString not in words:
                words[sortedString] = []
                words[sortedString].append(str)
            else:
                words[sortedString].append(str)
        
        anagramList = []
        for key, value in words.items():
            anagramList.append(value)
        
        return anagramList
        