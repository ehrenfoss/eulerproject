## This program is usfull for solving Euler Project #16
## 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
## What is the sum of the digits of the number 21000?

PowerDigitString = str(2**1000)
PowerDigitSum = 0

for i in range(0,len(PowerDigitString),1):
    PowerDigitSum += int(PowerDigitString[i])

print(PowerDigitSum)
