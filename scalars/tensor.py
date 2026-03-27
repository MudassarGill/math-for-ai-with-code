A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Addition:", result)




tarnspose=[[2,3,4],[5,6,7]]

result=[]

for i in range(len(tarnspose)):
    row=[]
    for j in range(len(tarnspose[0])):
        row.append(tarnspose[j][i])
    result.append(row)

print("Tarnspose:", result)


import numpy as np 

A = np.array([
    [1, 1],
    [1, -1]
])

B = np.array([10, 2])

X = np.linalg.solve(A, B)

print("Solution:", X)