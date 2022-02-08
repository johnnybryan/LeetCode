/**
 * @param {string} s
 * @return {boolean}
 */
// const validPalindrome = (s) => {
//   if (s.length < 2) return true;
//   s = s.toLowerCase().replace(/[^a-z0-9]/ig, '');
//   for (let i = 0; i < s.length; i++) {
//     sliced = s.slice(0, i) + s.slice(i);
//     console.log(sliced);
//     let left = 0;
//     let right = sliced.length - 1;
//     while (left <= right) {
//       if (sliced[left] !== sliced[right]) return false;
//       left++;
//       right--;
//     }
//   }
//   return true;
// };

const isTruePalindrome = function(s, p1, p2) {
  while (p1 < p2) {
    if (s[p1] !== s[p2]) return false;
    p1++;
    p2--;
  }
  
  return true;
}

/**
 * @param {string} s
 * @return {boolean}
 */
const validPalindrome = function(s) {
  let p1 = 0;
  let p2 = s.length - 1;
  
  while (p1 < p2) {
    if (s[p1] !== s[p2]) return isTruePalindrome(s, p1 + 1, p2) || isTruePalindrome(s, p1, p2 - 1);
    p1++;
    p2--;
  }
  
  return true;
}