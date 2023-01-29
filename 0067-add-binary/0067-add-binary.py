class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a), len(b))
        answer = [None for _ in range(length)]
        if len(a) < length:
            a = '0'*(length - len(a)) + a
        if len(b) < length:
            b = '0'*(length - len(b)) + b
        a = list(a)
        a.reverse()
        b = list(b)
        b.reverse()
        s, c = 0, 0
        for i in range(length):
            x = int(a[i])
            y = int(b[i])
            s = x + y + c
            if s > 1:
                c = 1
                s -= 2
            else:
                c = 0
            answer[i] = str(s)
        if c == 1:
            answer += ['1']
        answer.reverse()
        answer = ''.join(answer)
        return answer
            