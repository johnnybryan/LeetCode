/**
 * @param {number[]} nums
 * @return {number}
 */
const removeDuplicates = (nums) => {
  let i = k = 1;
  while (i < nums.length) {
    if (nums[k - 1] !== nums[i]) {
      nums[k] = nums[i];
      k++;
    }
    i++;
  }
  return k;
};