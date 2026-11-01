class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums and seen[complement] != i:
                return [i, seen[complement]]