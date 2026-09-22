class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for num in nums:
            groups[num] = groups.get(num, 0) + 1

        sorted_groups = sorted(groups.items(), key=lambda x: x[1])
        output = [item[0] for item in sorted_groups]
        return output[-k:]
