class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # mutiply all elements store in variable
        # iterate and divide and store value.
        # if list has 0 exclude and keep the mutiply values.
        # while diivide for 0 lists except 0 index make else 0 and store the mutiple in 0 index.

        all_multiple = 1
        output = [0] * len(nums)
        zero_count = nums.count(0)
        if zero_count == len(nums):
            return output
        for num in nums:
            if num == 0:
                continue
            else:
                all_multiple *= num

        for index, num in enumerate(nums):
            if zero_count == 1:
                if num == 0:
                    output[index] = all_multiple
                else:
                    output[index] = 0
                continue
            if zero_count > 1:
                if num == 0:
                    output[index] = 0
                else:
                    output[index] = 0
                continue
            output[index] = all_multiple // num
        return output

