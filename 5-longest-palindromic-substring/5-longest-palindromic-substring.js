/**
 * @param {string} s
 * @return {string}
 */
const longestPalindrome = (s) => {
  let longest = "";
  
  // define helper func to find palindromes
  const findLongest = (str, i, j) => {
    while (i >= 0 && j < str.length && str[i]===str[j]) {
      i--;
      j++;
    }
    return str.slice(i+1, j);
  }
  
  // iterate thru string
  for (i = 0; i < s.length; i++) {
    let currentLong = '';
    // find longest pal substring for even & odd length
    const oddPal = findLongest(s, i, i);
    const evenPal = findLongest(s, i, i + 1);
    
    // find longest between even and odd
    if (oddPal.length > evenPal.length) {
      currentLong = oddPal;
    } else {
      currentLong = evenPal;
    }
    
    // find longest
    if (currentLong.length > longest.length) {
      longest = currentLong;
    }
  }
  return longest;
};