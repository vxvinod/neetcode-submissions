class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        total_seq, last_total_seq = 0, 0
        nums = sorted(nums)
        print(nums)
        if not nums:
            return 0
        # if nums[len(nums)-1] - nums[0] == len(nums)-1:
        #     return len(nums)
        
        for index, num in enumerate(nums):
            if index == 0:
                last_num = num
                total_seq = 1
                continue
            if num - last_num == 0:
                continue
            if num - last_num == 1:
                total_seq += 1
            else:
                if total_seq > last_total_seq:
                    last_total_seq = total_seq
                total_seq = 1
            last_num = num

        return last_total_seq if last_total_seq > total_seq else total_seq
