/**
 * @param {string} columnTitle
 * @return {number}
 */
const titleToNumber = (string) => {
  let number = 0;
  for (let i = 0; i < string.length; i++){
      let char = string[(string.length - 1) - i];
      number += Math.pow(26, i) * (char.charCodeAt(0) - 64);
  } 
  return number;
};
