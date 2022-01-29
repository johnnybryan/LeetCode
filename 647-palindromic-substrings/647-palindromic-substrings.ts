const countSubstrings = (s: string): number => {
  let output = 0;
  const countPalindromes = (left: number, right: number): number => {
    let count = 0;
    while (left >= 0 && right <= s.length-1 && s[left]===s[right]) {
      count++;
      left--;
      right++;
    }
    return count;
  }
  for (let i = 0; i < s.length; i++) {
    output += countPalindromes(i, i);
    output += countPalindromes(i, i+1);
  }
  return output;
};