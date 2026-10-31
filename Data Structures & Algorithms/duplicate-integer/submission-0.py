class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenElements = set()
        for num in nums:
            seenElements.add(num)
        return len(nums) != len(seenElements)