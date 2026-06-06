class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}
        t_set = {}
        for char in s:
            if (char in s_set.keys()):
                s_set[char]+=1
            else:
                s_set[char] = 1

        for char in t:
            if (char in t_set.keys()):
                t_set[char]+=1
            else:
                t_set[char] = 1
        if (s_set == t_set and len(s)):
            return True
        return False
