class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        s_map, t_map = {}, {}
        for i in range(len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            t_map[t[i]] = t_map.get(t[i], 0) + 1
        for c in s_map:
            if s_map[c] != t_map.get(c, 0):
                return False
        return True
            
        