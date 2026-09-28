import math 
A=[
    [1,-2,3],
    [-4,5,-6]
]
rows = len(A)
cols =len(A[0])

for i in range(rows):
    sum_square =0
    for j in range(cols):
        sum_square+=A[i][j]**2
        
frobenius = math.sqrt(sum_square)
print(frobenius)
