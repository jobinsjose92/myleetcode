class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        
        if needle not in haystack:
            return -1
        
        return haystack.index(needle)
solution = Solution()
haystack = "Hello, how are you?"
needle = "how"
result = solution.strStr(haystack, needle)
print(result)