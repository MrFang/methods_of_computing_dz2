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

# Works ONLY with diagonal matrix
def getInverseMatrix(matrix):
    r =[]

    for i in range(len(matrix)):
        r.append([])
        
        for j in range(len(matrix[0])):

            if i == j:
                r.append(1/matrix[i][i])
            else:
                r.append(0)
    
    return r

def multMatrixByVec(m, v): 
    if len(m[0]) != len(v):
        raise ValueError("Incorrect dimensions M has %dx%d, but V has %d" %(len(m), len(m[0]), len(v)))

    r = []

    for i in range(len(m)):
        r.append(0)
        for j in range(len(m[0])):
            r[i] += m[i][j] * v[j]
    
    return r

def substractVectorFromVector(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Incorrect dimensions V1 has %d, but V2 has %d" %(len(v1), len(v2)))

    result = []

    for i in range(len(v1)):
        result.append(v1[i] - v2[i])
    
    return result;

def computeParams(A, y):
    B = []
    newY = []
    sums = []

    for i in range(len(A)):
        B.append([])
        newY.append(y[i] / A[i][i])
        sums.append(0)

        for j in range(len(A[0])):
            if i == j:
                B[i].append(0)
            else:
                a = A[i][j] / A[i][i]
                B[i].append(a)
                sums[i] += abs(a)

    return[B, newY, max(sums)]

def getFuncAndQ(A, y):
    [B, newY, q] = computeParams(A, y)

    def F(x):
        return substractVectorFromVector(newY, multMatrixByVec(B, x))
    
    return [F, q]

def findRoot(A, y):
    [f, q] = getFuncAndQ(A, y)
    x = [0 for elem in y]
    eps = float(input("Epsilon: "))
    threshold = eps * (1-q) / q

    while True:
        oldX = x
        x = f(x)

        if sqrt( sum( list( map(lambda x: x*x,  substractVectorFromVector(x, oldX)) ) ) ) < threshold:
            break;
    
    return x