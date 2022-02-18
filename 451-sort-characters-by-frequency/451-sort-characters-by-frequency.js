/**
 * @param {string} s
 * @return {string}
 */
const frequencySort = (s) => {
  const seen = {}; 
  let result = "";
  
  for (let char of s) { // store characters Frequency of given string in map
      seen[char] ? seen[char]++ : seen[char] = 1;
  }

  // sort characters according to characters Frequency in descending order
  const sortedArray = Object.keys(seen).sort((a,b)=>seen[b]-seen[a]);

  // iterate through sorted array and append character(character frequency) times to result  
  for (let char of sortedArray) {
    result += char.repeat(seen[char]);
  }
  
  return result;
};