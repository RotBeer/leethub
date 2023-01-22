class Solution:
    def isValid(self, s: str) -> bool:
        p_dict = {'{': '}', '[': ']', '(': ')'}
        stk = []
        for c in s:
            stk.append(c)
            if len(stk) > 1 and stk[-1] == p_dict.get(stk[-2]):
                stk = stk[:-2]
        return False if stk else True