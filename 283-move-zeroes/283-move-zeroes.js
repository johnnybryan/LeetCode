/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
const moveZeroes = function(nums) {
  let j = 0;  // nonzero count

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
	  // swap elements
      [nums[j], nums[i]] = [nums[i], nums[j]];
      j++;
    }
  }
};