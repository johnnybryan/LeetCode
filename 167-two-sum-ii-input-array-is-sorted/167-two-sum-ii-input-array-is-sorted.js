/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
const twoSum = (numbers, target) => {
  let left = 0;
  let right = numbers.length - 1;
  while (left < right) {
    const current = numbers[left] + numbers[right];
    if (current === target) {
      return [left + 1, right + 1];
    }
    if (current < target) left += 1;
    if (current > target) right -= 1;
  }
  return [-1, -1];
};