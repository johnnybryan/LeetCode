/**
 * @param {string} s
 * @return {number}
 */

// SLIDING WINDOW
// const lengthOfLongestSubstring = (s) => {
//   const map = {};
//   let start = 0, max = 0;
//   for (let end = 0; end < s.length; end++) {
//     const char = s[end];
//     if (char in map) {
//       start = Math.max(start, map[char]+1);
//     }
//     map[char] = end;
//     max = Math.max(max, end - start + 1);
//   }
//   return max;
// };

// SLIDING WINDOW / TWO POINTER #2

const lengthOfLongestSubstring = str => {
  if (!str) return 0;
  const set = new Set();
  let l = 0;
  let r = 0;
  let substring = 0;
  while (l < str.length && r < str.length) {
    if (set.has(str[r])) {
      set.delete(str[l]);
      l++;
    } else {
      set.add(str[r]);
      substring = Math.max(substring, set.size);
      r++;
    }
  }
  return substring;
};