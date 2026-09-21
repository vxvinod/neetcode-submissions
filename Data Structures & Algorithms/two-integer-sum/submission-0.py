class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            remain = target - value
            if remain in seen.keys():
                return [seen[remain], index]
            seen[value] = index