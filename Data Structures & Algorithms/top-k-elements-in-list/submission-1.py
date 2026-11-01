class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        valuesList = []
        for key, value in count.items():
            valuesList.append(value)
        
        sortedList = sorted(valuesList)
        topK = sortedList[-k:]
        
        finalList = []
        for key, value in count.items():
            if value in topK:
                finalList.append(key)
        
        return finalList