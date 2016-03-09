## This program is for solving Euler Project problem #17
## If the numbers 1 to 5 are written out in words: one, two, three, four, five,
## then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
##
## If all the numbers from 1 to 1000 (one thousand) inclusive were written out
## in words, how many letters would be used?
##
## NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
## forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
## 20 letters. The use of "and" when writing out numbers is in compliance with
## British usage.

## Initialize array
NumberOfWords = [[]]*1000

## Start the matrix by entering the words for 1-19 and 20, 30, .. ,90
NumberOfWords[0] = len('one')
NumberOfWords[1] = len('two')
NumberOfWords[2] = len('three')
NumberOfWords[3] = len('four')
NumberOfWords[4] = len('five')
NumberOfWords[5] = len('six')
NumberOfWords[6] = len('seven')
NumberOfWords[7] = len('eight')
NumberOfWords[8] = len('nine')
NumberOfWords[9] = len('ten')
NumberOfWords[10] = len('eleven')
NumberOfWords[11] = len('twelve')
NumberOfWords[12] = len('thirteen')
NumberOfWords[13] = len('fourteen')
NumberOfWords[14] = len('fifteen')
NumberOfWords[15] = len('sixteen')
NumberOfWords[16] = len('seventeen')
NumberOfWords[17] = len('eighteen')
NumberOfWords[18] = len('nineteen')
NumberOfWords[19] = len('twenty')
NumberOfWords[29] = len('thirty')
NumberOfWords[39] = len('forty')
NumberOfWords[49] = len('fifty')
NumberOfWords[59] = len('sixty')
NumberOfWords[69] = len('seventy')
NumberOfWords[79] = len('eighty')
NumberOfWords[89] = len('ninety')

## Calculate the first hundred
## This loop ounts letters of 21 - 29, then 31 - 39, up to 91 - 99                   
for i in range(20,100,10):
    for j in range(0,9,1):
        NumberOfWords[i+j] = NumberOfWords[i-1] + NumberOfWords[j]

## This loop counts letters for 100, 200, ... 900
for i in range(1,10,1):
    NumberOfWords[i*100-1] = NumberOfWords[i-1] + len('hundred')

## This loop fills in the rest of the array
for j in range(100,1000,100):
    for i in range(0,99,1):
        NumberOfWords[j+i] = NumberOfWords[j-1] + len('and') + NumberOfWords[i]

## The Capstone
NumberOfWords[999] = NumberOfWords[0] + len('thousand')

## The answer
print('Answer:',sum(NumberOfWords))
