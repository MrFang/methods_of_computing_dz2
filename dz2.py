from utils import readMatrixFromFile
from iterationMethod import findRoot

A1 = readMatrixFromFile('input22_A1.txt')
y1 = readMatrixFromFile('input22_y1.txt')
print('First root:', findRoot(A1, y1))

A2 = readMatrixFromFile('input22_A2.txt')
y2 = readMatrixFromFile('input22_y2.txt')
print('Second root:', findRoot(A2, y2))
