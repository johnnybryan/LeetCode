class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word in grouped_anagrams:
                grouped_anagrams[sorted_word].append(word)
            else:
                grouped_anagrams[sorted_word] = [word]
        return grouped_anagrams.values()