from utils import readMatrixFromFile

def divideIntoTwoMatrices(matrix):
    C, D = list(), list()

    for i, row in enumerate(matrix):
        C.append(list())
        D.append(list())
        
        for j, elem in enumerate(row):
            
            if i == j:
                C[i].append(0)
                D[i].append(elem)
            else:
                C[i].append(elem)
                D[i].append(0)

    return [C, D]

def getInverseMatrix(matrix): 
    raise NotImplementedError

def multMatrixByMatrix(m1, m2):
    raise NotImplementedError

def substractMatrixFromMatrix(m1, m2):
    raise NotImplementedError

def computeQ(matrix):
    raise NotImplementedError

def getFuncAndQ(A, y):
    [C, D] = divideIntoTwoMatrices(A)
    inverseC = getInverseMatrix(C);
    B = multMatrixByMatrix(inverseC, D)
    newY = multMatrixByMatrix(inverseC, y)
    q = computeQ(B)

    def F(x):
        return substractMatrixFromMatrix(newY, multMatrixByMatrix(B, x))
    
    return [F, q]

A1 = readMatrixFromFile('input22_A1.txt')
y1 = readMatrixFromFile('input22_y1.txt')

[f, q] = getFuncAndQ(A1, y1)

# TODO: Implement iterations
