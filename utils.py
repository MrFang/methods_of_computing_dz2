def readMatrixFromFile(filename):
    with open(filename, 'r') as f:
        s = f.read();
    a = s.split('\n');
    a = a[1:];
    for idx, val in enumerate(a):
        a[idx] = val.split(" ")      
    
    a=[[int(elem) for elem in row]for row in a]

    return a if len(a) > 1 else a[0]
    