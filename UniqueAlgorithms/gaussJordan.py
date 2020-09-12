import numpy as np
import sys

unknowns = int(input("Enter a number of unknowns: "))

a = np.zeros((unknowns, unknowns + 1))

x = np.zeros(unknowns)

print('Enter Augmented Matrix Coefficients:')
for i in range(unknowns):
    for j in range (unknowns + 1):
        a[i][j] = float (input('a[' + str(i) + '] [' + str(j) + ']= '))


for i in range(unknowns):
    if a[i][i] == 0.0:
        sys.exit('Divide by zero detected!')

    for j in range(unknowns):
        if i != j:
            ratio = a[j][i]/a[i][i]

            for k in range (unknowns + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]


for i in range (unknowns):
    x[i] = a[i][unknowns]/a[i][i]


print('\nRequired solution is: ')
for i in range(unknowns):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')

