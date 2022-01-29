/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
// merge interval method
// time: O(Nlog(N)) space: O(N)
const merge = (intervals) => {
  if (intervals.length < 2) return intervals;
  
  intervals.sort((a,b) => a[0] - b[0]);
  const merged = [];
  merged.push(intervals[0]);
  
  for (let i = 1; i < intervals.length; i++) {
    let prev = merged.pop();
    let curr = intervals[i];
    if (prev[1] >= curr[0]) merged.push([prev[0], Math.max(prev[1], curr[1])]);
    else merged.push(prev, curr)
  }
  return merged;
};