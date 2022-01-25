/**
 * @param {number[]} nums
 * @return {boolean}
 */
// GREEDY ALGORITHM
const canJump = (nums) => {
  // iterate thru nums array
  let i = 0;
  let max = 0;
  let target = nums.length - 1;
  while (i < nums.length) {
    max = Math.max(max, i + nums[i]);
    if (max >= target) return true;
    if (max <= i && nums[i] === 0) return false;
    i++;
  }
  return false
};