/**
 * @param {number} n
 * @return {number}
 */
// SIEVE OF ERATOSTHENES
const countPrimes = (n) => {
  // create array of all nums from 0 to n and assign values to true/prime
  const isPrime = new Array(n).fill(true);
  // assign count variable to 0
  let count = 0;
  // mark index 0 and 1 as false/not prime
  isPrime[0] = false;
  isPrime[1] = false;
  // iterate through array, as long as i^2 is less than n
  for (let i = 2; i * i < n; i++) {
    // if element is false/not prime, skip
    if (!isPrime[i]) continue;
    // else find i^2 and all incremenations by i as long as it's less than n
    for (let j = i * i; j < n; j += i) {
      isPrime[j] = false; // assign to false/not prime
    }
  }
  // iterate through the array
  for (let k = 2; k < n; k++) {
    if (isPrime[k]) count++; // if prime, increment count
  }
  return count;
};