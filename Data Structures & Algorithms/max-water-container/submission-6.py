class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # find the heighest bar.
        # then iterate and if lower keey h and i as b
        # do h*b and store area 
        # return max area
        # area = []
    
        # for i, height in enumerate(heights):
        #     for j, h in enumerate(heights[i+1:]):
        #         l = min(height, h)
        #         b = j+1
                
        #         area.append( l * b)
        # return max(area)
        left = 0
        right = len(heights) - 1
        area = 0

        while left < right:
            l = min(heights[left], heights[right])
            b = right - left
            area = max(area, l*b)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return area