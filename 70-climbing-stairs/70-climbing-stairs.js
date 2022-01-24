/**
 * @param {number} n
 * @return {number}
 */

// memoized top down DP solution
const climbStairs = (n, memo = {}) => {
  if (n===1) return 1;
  if (n===2) return 2;
  if (!memo[n]) memo[n] = climbStairs(n-1, memo) + climbStairs(n-2, memo);
  return memo[n]
}