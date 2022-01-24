/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
// BFS
// TIME: O(N*M*26), SPACE: O(N)
const ladderLength = (beginWord, endWord, wordList) =>{
  const dictionary = new Set(wordList);
  let queue = [beginWord];
  let steps = 1;
  while (queue.length) {
    const next = [];
    for (let word of queue) {
      if (word === endWord) return steps;
      for (let i = 0; i < word.length; i++) {
        for (let j = 0; j < 26; j++) {
          const newWord = word.slice(0, i) + String.fromCharCode(j + 97) + word.slice(i + 1);
          if (dictionary.has(newWord)) {
            next.push(newWord);
            dictionary.delete(newWord);
          }
        }
      }
    }
    queue = next;
    steps++;
  }
  return 0;
};