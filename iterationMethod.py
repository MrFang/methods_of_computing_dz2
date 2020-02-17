from math import sqrt

def divideIntoTwoMatrices(matrix):
    C, D = [], []

    for i, row in enumerate(matrix):
        C.append([])
        D.append([])
        
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
    sums = []
    
    for i, row in enumerate(matrix):
        sums.append(0)

        for j, elem in enumerate(row):
            if j != i:
                sums[i] += abs(elem / matrix[i][i])

    return max(sums)

def getFuncAndQ(A, y):
    [C, D] = divideIntoTwoMatrices(A)
    inverseC = getInverseMatrix(C);
    B = multMatrixByMatrix(inverseC, D)
    newY = multMatrixByMatrix(inverseC, y)
    q = computeQ(B)

    def F(x):
        return substractMatrixFromMatrix(newY, multMatrixByMatrix(B, x))
    
    return [F, q]

def findRoot(A, y):
    [f, q] = getFuncAndQ(A, y)
    x = [0 for elem in y]
    eps = input("Epsilon: ")
    threshold = eps * (q-1) / q

    while True:
        oldX = x
        x = f(x)

        if sqrt( sum( list( map(lambda x: x*x,  substractMatrixFromMatrix(x, oldX)) ) ) ) < threshold:
            break;
    
    return x