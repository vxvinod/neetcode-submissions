class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # check l, r near the target.
        # rotate the opp pointer
        # check mid or opp pointer matches the target
        # if match return else repeat.
        left  = 0
        right = len(nums) - 1
        print(left, right)
        if (left == right == 0):
            if nums[left] == target: 
                return 0
            else:
                return -1
        while left <= right:
            mid = (right + left) // 2
            #print(f"left-#{left}--right-#{right}--mid-#{mid}")
            if nums[mid] == target:
                return mid
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right

            #nearer = "right" if ((nums[right] - target) < (nums[left] - target)) else "left"
            # if(nums[right] - target) < (nums[left] - target):
            #     left = mid + 1
            # else:
            #     right = mid 
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid] : 
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target < nums[right]:
                    left = mid + 1
                else:
                    right = mid

        return -1