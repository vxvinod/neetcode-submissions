class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Have right and left pointer, left is 0 and right is last element
        # mid = right - left /2
        # if mid value < right value r = mid else l = mid+1
        # run while till left < right reutrn the left value.

        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            count +=1
            #print(f"count-#{count}")
            mid =(right + left) // 2
           # print(left, mid, right)
           # print(f"nums #{nums[left]}, #{nums[right]}")
            if nums[mid] > nums[right]:
                left = (mid + 1)
               # print(f"shift lef #{left} and right #{right}")
            else:
                right = mid 
               # print(f"shift right #{right}")

        return nums[left]