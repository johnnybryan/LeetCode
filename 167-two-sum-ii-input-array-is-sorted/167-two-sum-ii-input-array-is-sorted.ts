const twoSum = (numbers: number[], target: number) : number[] => {
  let left:number = 0;
  let right:number = numbers.length - 1;
  while (left < right) {
    const current:number = numbers[left] + numbers[right];
    if (current === target) return [left + 1, right + 1];
    if (current < target) left += 1;
    if (current > target) right -= 1;
  }
  return [-1, -1]
};