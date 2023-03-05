class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = {}
        ts = {}
        for i in range(len(s)):
            if not st.get(s[i]) and not ts.get(t[i]):
                st[s[i]] = t[i]
                ts[t[i]] = s[i]
            elif st.get(s[i]) and st.get(s[i]) == t[i]:
                continue
            else:
                return False
                        
        return True
