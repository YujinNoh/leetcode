# version1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_t = t
        for i in s:
            t= t.replace(i, "", 1)
        
        for j in new_t:
            s = s.replace(j, "", 1)
        
        return True if (t == "") and (s == "") else False
# version2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))
