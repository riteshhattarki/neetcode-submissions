class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = freq.get(num, 0) + 1
            else:
                freq[num] += 1

        valueList = []
        for value in freq.values():
            valueList.append(value)
        
        sortedList = sorted(valueList)
        lastKElements = sortedList[-k:]

        finalList = []
        for key, value in freq.items():
            if value in lastKElements:
                finalList.append(key)
        
        return finalList