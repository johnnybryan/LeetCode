function lengthOfLongestSubstring(s: string): number {
  let start = 0;
  let maxLength = 0;
  const charMap = {};
  for (let end = 0; end < s.length; end++) {
    let lastChar = s[end];
    if (lastChar in charMap) {
      start = Math.max(start, charMap[lastChar] + 1)
    }
    charMap[lastChar] = end;
    maxLength = Math.max(maxLength, end - start + 1);
  }
  return maxLength;
};