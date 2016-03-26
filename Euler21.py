## ProjectEuler.net Problem #21
## Let d(n) be defined as the sum of proper divisors of n
## (numbers less than n which divide evenly into n).
## If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
## and each of a and b are called amicable numbers.
##
## For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
## 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of
## 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
##
## Evaluate the sum of all the amicable numbers under 10000.
import math

global i,j,k,result
result = 0

def d(x):
    amicable = 0
    for i in range(1,x,1):
        if x%i == 0:
            amicable += i
    return amicable

for j in range(0,10000,1):
    for k in range(1,j+1,1):
        if j != k and d(j) == k and d(k) == j:
            print("AMICABLE PAIRS!!:",j," & ",k)
            result += j+k

print('Answer: ',result)    
