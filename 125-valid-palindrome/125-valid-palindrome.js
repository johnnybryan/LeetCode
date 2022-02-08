/**
 * @param {string} s
 * @return {boolean}
 */

const isPalindrome = (s) => {
    s = s.toLowerCase().replace(/[^a-z0-9]/ig, '');
    if (s.length < 2) return true;
    let i = 0;
    let j = s.length - 1;
    while (i <= j) {
        if (s[i] !== s[j]) return false;
        i++;
        j--;
    }
    return true;
};