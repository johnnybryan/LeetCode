class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        max_left = height[0]
        max_right = height[-1]
        point_left = 1
        point_right = len(height) - 2
        rain_water = 0
        
        while point_left <= point_right:
            if max_left < height[point_left]:
                max_left = height[point_left]
            if max_right < height[point_right]:
                max_right = height[point_right]
                
            if max_left < max_right:
                rain_water += max_left - height[point_left]
                point_left += 1
            else:
                rain_water += max_right - height[point_right]
                point_right -= 1
        return rain_water