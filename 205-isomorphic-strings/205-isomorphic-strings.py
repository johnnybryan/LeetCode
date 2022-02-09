class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map = {}
        i = 0
        while (i < len(s)):
            if s[i] not in hash_map:
                if t[i] in hash_map.values():
                    return False
                else:
                    hash_map[s[i]] = t[i]
            else:
                if hash_map[s[i]] != t[i]:
                    return False
            i += 1
        return True