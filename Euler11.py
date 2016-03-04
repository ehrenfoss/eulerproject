## Takes a 20 by 20 array and finds the highest product of any 4 adjacent (linearly, horizontaly, or diagnonaly) numbers""
"""Usefull for solving Project Euler problem #11"""
SquareNumbers = []
## Open the data set
Square20 = [line.rstrip('\n') for line in open("/Users/mattmawson/Documents/The 400.txt")]

#Parse ASCII string into a comma delimited list
for num in range(0,20):
    SquareNumbers += Square20[num].split()
    
## Temporary variables used in processing quadruples
maxNum = 0
HorizValue = 0
VerticalValue = 0
LeftToRightDiagonal = 0
RightToLeftDiagonal = 0

## This block checks all quadruples on the horizontal grid to find the max product
## FYI the data set is treated as a single 400 item list with no line breaks.
for num in range(0,397):
    HorizValue = int(SquareNumbers[num])*int(SquareNumbers[num+1])*int(SquareNumbers[num+2])*int(SquareNumbers[num+3])
    if HorizValue > maxNum:
        print('HORIZ WON:',num)
        print(HorizValue)
        maxNum = HorizValue

## This block checks all the quadruples in the vertical grid
for foo in range(0,19,1):
    for num in range(foo,320+foo,20):
        VerticalValue = int(SquareNumbers[num])*int(SquareNumbers[num+20])*int(SquareNumbers[num+40])*int(SquareNumbers[num+60])
        if VerticalValue > maxNum:
            print('VERT WON:',num,' ',foo)
            print(VerticalValue)
            maxNum = VerticalValue
            
## This block checks the left to right diagonals
for bar in range(0,336,1):
    LeftToRightDiagonal = int(SquareNumbers[bar])*int(SquareNumbers[bar+21])*int(SquareNumbers[bar+21*2])*int(SquareNumbers[bar+21*3])
    if LeftToRightDiagonal > maxNum:
        print('Left To Right Diagonal WON:',bar)
        print(LeftToRightDiagonal)
        maxNum = LeftToRightDiagonal

## This block checks the right to left diagonals
for boo in range(3,339,1):
    RightToLeftDiagonal = int(SquareNumbers[boo])*int(SquareNumbers[boo+19])*int(SquareNumbers[boo+19*2])*int(SquareNumbers[boo+19*3])
    if RightToLeftDiagonal > maxNum:
        print('Right to Left Diagonal WON:',boo)
        print(RightToLeftDiagonal)
        maxNum = RightToLeftDiagonal
