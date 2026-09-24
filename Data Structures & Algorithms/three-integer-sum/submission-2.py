class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       # seen = {}
        output = []
        added = set()
        for i, num in enumerate(nums):
            target = -num
            seen = {}
            for j, n in enumerate(nums[i+1:]):
                remain = target - n
                if remain in seen:
                    sort_i = sorted([nums[i], n, remain])
                    key = tuple(sort_i)
                    if key not in added:
                        output.append(sort_i)
                        added.add(key)
                seen[n] = True
                
        return output