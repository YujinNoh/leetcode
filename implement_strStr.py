class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        elif needle not in haystack:
            return -1
        else:
            haystack = haystack.replace(needle, "*")
            return haystack.index("*")
