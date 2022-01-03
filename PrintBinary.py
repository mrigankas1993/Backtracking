# all possible possible binary numbers with same number of digit as the integer parameter
''' 14 CS 106B lecture Backtracking printBinary, printDecimal my Python implementation'''
def printBinary(digit, choosen):
    if digit  == 0:
        print(choosen)
        return
    for nos in range(2):
        choosen += str(nos) #choose
        printBinary(digit - 1, choosen) #explore
        choosen = choosen[:len(choosen) - 1] #unchoose , backtracking

printBinary(5, "")
    
    
    
