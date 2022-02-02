/**
 * @param {number[]} nums
 * @return {number}
 */
// Kadane's algorithm
const maxSubArray = (nums) => {
    if (!nums || nums.length === 0) return 0;
    let cur = nums[0];
    let max = nums[0];
    for (let i = 1; i < nums.length; i++) {
        cur = Math.max(nums[i], cur + nums[i]);
        max = Math.max(max, cur);
    }
    return max;
};