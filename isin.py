def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # bisection search
    cp = int(len(aStr)/2) # initial check point
    if char == aStr[cp]:
        # print(aStr[cp])
        # print("1")
        return True
    elif char < aStr[0] or char > aStr[-1]:
        # print(aStr[0], aStr[-1])
        # print("2")
        return False
    elif char < aStr[cp]:
        return isIn(char, aStr[:cp])
        # print(aStr[:cp])
    else: # char > aStr[cp]
        return isIn(char, aStr[cp:])
        # print(aStr[:cp])

c = 'b'
s = 'abcdef'
if isIn(c,s):
    print("found")
else:
    print("Not found")
