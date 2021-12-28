"""
Визначити суму додатних елементів матриці вище побічної діагоналі.
"""
import random
m = int(input('m = '))
n = int(input('n = '))
A = [ [random.randint(-100, 101) for j in range(n)] for i in range(m) ]
print("A = ")
for i in range(m):
    print(A[i])
sum=0
n = len(A)
for i in range(n):
    for j in range(n - (i + 1)):
        if A[i][j] > 0:
            sum += A[i][j]
print(sum)