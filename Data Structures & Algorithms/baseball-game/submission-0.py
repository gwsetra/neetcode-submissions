class Solution:
    def calPoints(self, operations: List[str]) -> int:
        op = []
        idx = -1

        for i in range(len(operations)):
            if '0' <= operations[i] <= '9':
                op.append(int(operations[i]))
                idx += 1
            elif operations[i] == '+':
                print('+')
                sums = op[idx] + op[idx-1]
                print(sums)
                op.append(sums)
                idx += 1
                print(op)
            elif operations[i] == 'C':
                print('C')
                op.pop(idx)
                idx -= 1
                print(op)
            elif operations[i] == 'D':
                print('D')
                sums = op[idx] * 2
                op.append(sums)
                idx += 1
        print(op)
        return sum(op)