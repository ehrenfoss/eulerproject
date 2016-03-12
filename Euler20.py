import math
## Factorial digit sum
## Euler Project Problem 20
## n! means n × (n − 1) × ... × 3 × 2 × 1
##
## For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
## and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
##
## Find the sum of the digits in the number 100!

# 100! has 158 terms
x = 100
MathFun = str(math.factorial(x)) # 100! as a string
MathFunDigits = [[]]*len(MathFun) # initialize array for storing individual digits of 100!
SumCounter = 0 # var for summing the digits

for i in range(0,len(MathFun),1): # Take the MathFun str and create array of the digits
    MathFunDigits[i] = MathFun[i]

for i in range(0,len(MathFun),1): # Sum the digits in the array
    SumCounter += int(MathFunDigits[i])

print('Answer:',SumCounter)
                      
    
