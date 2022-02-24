/**
 * @param {number[]} height
 * @return {number}
 */
const maxArea = function(height) {
    let max = 0,
        left = 0,
        right = height.length - 1;
    while (left < right) {
        let current = (right - left) * Math.min(height[left], height[right]);
        max = Math.max(max, current);
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return max;
};