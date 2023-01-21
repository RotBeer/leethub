class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        prefix = max(strs, key = lambda x: len(x))
        for i in range(len(prefix)):
            for s in strs:
                if not s.startswith(prefix):
                    break
            else:
                break
            prefix = prefix[:-1]

        return prefix