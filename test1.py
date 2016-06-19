from random import randint

class Answer:
    def __init__(self, x, y, z, result):
        self.a = x
        self.b = y
        self.c = z
        self.sum = result

def getSum(Matrix):
    sumMatrix = 0
    for row in Matrix:
        sumMatrix += sum(row)
    return sumMatrix

def getBest3OrtogonalColumns(Matrix):
    answers = []
    for i in range(10):
        a = Matrix[i]
        for j in range(10):
            b = [Matrix[l][j] for l in range(10) if l != i]
            for k in range(10):
                c = [[Matrix[l][m][k] for m in range(10) if m != j] for l in range(10) if l != i]
                answers.append(Answer(i+1, j+1, k+1, getSum(a) + getSum(b) + getSum(c)))
    return sorted(answers, key=lambda x: x.sum, reverse=True)[0]

My3dMatrix = [[[randint(0, 9) for _ in range(10)] for _ in range(10)] for _ in range(10)]
answer = getBest3OrtogonalColumns(My3dMatrix)
print("From first dimension choose %d vector" % answer.a)
print("From second dimension choose %d vector" % answer.b)
print("From third dimension choose %d vector" % answer.c)
print("Sum for this vectors is %d" % answer.sum)
