class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        count = {}
        for i in range(len(strs)):
            sortedList = sorted(strs[i])
            sortedString = "".join(sortedList)
            if sortedString not in count:
                count[sortedString] = []
                count[sortedString].append(strs[i])
            else:
                count[sortedString].append(strs[i])
        
        finalList = []
        for key, value in count.items():
            finalList.append(value)
        
        return finalList