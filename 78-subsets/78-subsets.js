/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const subsets = function(nums) {
  const subsets = [];
  subsets.push([]);
  for (let i = 0; i < nums.length; i++) {
    const current = nums[i];
    const len = subsets.length;
    for (let j = 0; j < len; j++) {
      const subset = subsets[j].slice(0);
      subset.push(current);
      subsets.push(subset);
    }
  }
  return subsets; 
};