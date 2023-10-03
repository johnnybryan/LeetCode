class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, max_area = 0, len(height) - 1, 0
        while l < r:
            min_height = min(height[l], height[r])
            length = r - l
            area = min_height * length
            max_area = max(area, max_area)
            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1
        return max_area
            