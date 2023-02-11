class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        for i in range(1, numRows):
            # tmp = [1]
            # for j in range(i-1):
            #     tmp.append(output[i-1][j] + output[i-1][j+1])
            # tmp.append(1)
            tmp = [1] + [output[i-1][j] + output[i-1][j+1] for j in range(i-1)] + [1]
            output.append(tmp)

        return output
