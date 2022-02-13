/**
 * @param {string} s
 * @return {boolean}
 */

const isValid = (s) => {
  const stack = [];
  const map = {
    '(':')',
    '{':'}',
    '[':']'
  };
  for (let char of s) {
    if (char === '(' || char === '{' || char === '[') {
      stack.push(char);
    } else if (map[stack.pop()] !== char) {
      return false;
    }
  }
  return !stack.length;
}