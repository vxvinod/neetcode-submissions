class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # iterate the numbers and subract the target and get the remain
        # check remain in numbers get the index
        seen = {}
        for index, num in enumerate(numbers):
            remain = target - num
            try:
                if remain in seen:
                    return [seen[remain], index+1]
                seen[num] = index+1
                # second_index = numbers.index(remain)
                # return [index+1, second_index+1]
            except:
                continue

