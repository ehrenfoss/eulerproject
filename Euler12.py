## Euler12.py is a program for finding the first Triangular Number with more than 500 factors
## This program takes roughly 48 hours to complete
import math
## Initialize Variables
SearchMatrixSize = 20000
Integers = [[]]*SearchMatrixSize
Triangles = [[]]*SearchMatrixSize

for i in range(0,SearchMatrixSize,1):
    Integers[i] = i+1

## Create the array of Triangular numbers to factor
## SearchMatrixSize was an arbitrarily chosen number for the range of Triangular Numbers to search
for j in range(0,SearchMatrixSize,1):
    Triangles[j] = sum(Integers[0:j])

## This function factors integers and creates a list of factors using modulus arithmatic.
## It prints numbers with more than 200 factors and quits when a number with 500 factors is found!
## Otherwise it runs silently
def Factor(x):
    FactorsList = []
    for k in range(1,math.floor(x/2)+1,1):
        if x%k == 0:
            FactorsList.append(k)

    if len(FactorsList) > 200:
        print(x,':',len(FactorsList),' : ',FactorsList)

    if len(FactorsList) > 500:
        print("WOO HOO!!!")
        print(x)
        exit()

## These 2 lines call Factor(x) to compute the list of factors for every number in the list "Triangles", which is 0 through SearchMatrixSize
## Already searched the first 8,384 triangular numbers
## The best is 592,416 with 107 factors
for l in range(0,len(Triangles),1):
    Factor(Triangles[l])
## The answer is 76,576,500
