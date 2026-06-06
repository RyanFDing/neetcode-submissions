class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1, set2 = {}, {}
        if (len(s) != len(t)):
            return False
        for i in range (len(s)):
            set1[s[i]] = set1.get(s[i], 0) + 1
            set2[t[i]] = set2.get(t[i], 0) + 1
        for element in set1:
            if (set1[element] != set2.get(element, 0)):
                return False
        return True
