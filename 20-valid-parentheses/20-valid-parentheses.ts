function isValid(s: string): boolean {
  const charMap = {
    '(':')',
    '[':']',
    '{':'}'
  };
  const stack = [];
  for (let char of s) {
    if (char in charMap) {
      stack.push(char);
    } else if (charMap[stack.pop()] !== char) {
      return false;
    }
  }
  return !stack.length;
};