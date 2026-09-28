A=[
    [1,-2,3],
    [-4,5,-6]
]
rows = len(A)
cols =len(A[0])
max_row_sum =0

for i in range(rows):
    row_sum=0
    for j in range(cols):
        row_sum+=abs(A[i][j])
        
    if row_sum>max_row_sum:
        max_row_sum=row_sum
        
print("infinity norm is",max_row_sum)