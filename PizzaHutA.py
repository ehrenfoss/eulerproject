## http://blog.pizzahut.com/flavor-news/national-pi-day-math-contest-problems-are-here-2/
## Problem A
## I’m thinking of a ten-digit integer whose digits are all distinct.
## It happens that the number formed by the first n of them is divisible
## by n for each n from 1 to 10. What is my number?
import math

global i

for i in range(123456780,9876543210,10):
    if '1' in str(i) and '2' in str(i) and '3' in str(i) and '4' in str(i) and '5' in str(i) and '6' in str(i) and '7' in str(i) and '8' in str(i) and '9' in str(i) and '0' in str(i) and int(str(i)[0:1])%1 == 0 and int(str(i)[0:2])%2 == 0 and int(str(i)[0:3])%3 == 0 and int(str(i)[0:4])%4 == 0 and int(str(i)[0:5])%5 == 0 and int(str(i)[0:6])%6 == 0 and int(str(i)[0:7])%7 == 0 and int(str(i)[0:8])%8 == 0 and int(str(i)[0:9])%9 == 0 and int(str(i)[0:10])%10 == 0:
       print(i)

