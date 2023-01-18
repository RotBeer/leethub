class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        roman_dict2 = {'IV': 4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM': 900}
        answer = 0
        while s:
            if s[:2] in roman_dict2.keys():
                token = s[:2]
                answer += roman_dict2[token]
                s = s[2:]
            else:
                token = s[:1]
                answer += roman_dict1[token]
                s = s[1:]
        return answer