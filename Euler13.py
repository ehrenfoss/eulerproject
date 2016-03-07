## Euler Project 13

## -- Below is the problem --
## The following iterative sequence is defined for the set of positive integers:
##
## n → n/2 (n is even)
## n → 3n + 1 (n is odd)
##
## Using the rule above and starting with 13, we generate the following sequence:
##
## 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
## It can be seen that this sequence (starting at 13 and finishing at 1) contains
## 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
## that all starting numbers finish at 1.
##
## Which starting number, under one million, produces the longest chain?
##
## NOTE: Once the chain starts the terms are allowed to go above one million.


## This is a recursive funtion, CollatzStep. It addes the input, x, to the end of the list CollatzChain
## and then applies the even/odd formula and calls itself until the input is 1
def CollatzStep(x):
    if x%2 == 0:
        CollatzChain.append(x)
        CollatzStep(x/2)
    elif x == 1:
        CollatzChain.append(1)
        return 1
    else:
        CollatzChain.append(x)
        CollatzStep(3*x+1)

global CollatzChain        
MaxChainSize = 0
MaxCollatzChain = []

## This runs CollatzStep on every number under a million and counts the length of the chains.
## The largest Collatz Sequence is saved to variable MaxCollatzChain and the starting number
## and chain size are spit out (i.e. printed) on the last 2 lines.

## My program searches from 1 to a million, but I saw that in the message board, somone posted a
## solution that searches 500001 to 1000000 step 2.  I can't figure out how they reduced the search
## space by so much.  @EOF any clues?

for i in range(1,1000000,1):
    CollatzChain = []
    CollatzStep(i)
    if len(CollatzChain) > MaxChainSize:
            MaxCollatzChain = CollatzChain
            MaxChainSize = len(CollatzChain)
            HighNum = i

print(MaxCollatzChain)  ## a 525 item list
print('Highest Number =',HighNum,' : ChainSize =',MaxChainSize)  ## should spit out 837799 & 525
