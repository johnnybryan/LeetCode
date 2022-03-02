/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
const checkInclusion = function(s1, s2) {
  
  if (s1.length > s2.length) {
    return false;
  }
  
  let chars = {};
  
  for (let i = 0; i < s1.length; i++) {
    if (!chars[s1[i]]) chars[s1[i]] = 0;
    chars[s1[i]]++;
  };
  
  let left = 0, right = 0, permLen = s1.length;
  
  while (right < s2.length) {
    
    if (chars[s2[right]] > 0) permLen--;
    
    chars[s2[right]]--;
    
    right++;
    
    if (permLen === 0) return true;
    
    if (right - left === s1.length) {
      if (chars[s2[left]] >= 0) {
        permLen++;
      }
      chars[s2[left]]++;
      left++;
    }
  }
  return false;
};