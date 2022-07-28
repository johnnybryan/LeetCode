/**
 * Encodes a list of strings to a single string.
 *
 * @param {string[]} strs
 * @return {string}
 */
const encode = (strs) => {
    return strs.join('johnny')
};

/**
 * Decodes a single string to a list of strings.
 *
 * @param {string} s
 * @return {string[]}
 */
const decode = (s) => {
    return s.split('johnny');
};

/**
 * Your functions will be called as such:
 * decode(encode(strs));
 */