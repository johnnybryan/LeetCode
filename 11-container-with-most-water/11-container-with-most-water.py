class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area, l, r = 0, 0, len(height) - 1
        while l < r:
            area = (r - l) * (min(height[l], height[r]))
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area