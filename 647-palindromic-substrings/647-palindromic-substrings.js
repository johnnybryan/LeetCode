/**
 * @param {string} s
 * @return {number}
 */
const countSubstrings = (s) => {
  let output = 0;
  const countPalindromes = (left, right) => {
    let count = 0;
    while (left >= 0 && right <= s.length-1 && s[left]===s[right]) { // checks if left equals right, expands outward
      left--;
      right++;
      count++;
    }
    return count;
  }
  for (let i = 0; i < s.length; i++) { // iterates through input string
    output += countPalindromes(i, i); // handles odd-length string
    output += countPalindromes(i, i+1); // handles even-length string
  }
  
  return output;
};