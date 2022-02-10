/**
 * @param {number[]} prices
 * @return {number}
 */
// KADANE'S ALGORITHM
const maxProfit = (prices) => {
  let max = 0;
  let current = 0;
  for (let i = 1; i < prices.length; i++) {
    let delta = prices[i] - prices[i-1];
    current += delta;
    if (current < 0) current = 0;
    max = Math.max(max, current);
  }
  return max;
};