def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # bisection search
    cp = int(len(aStr)/2) # initial check point
    if char == aStr[cp]:
        # print(aStr[cp])                        # for debug
        # print("1")                             # for debug
        return True
    elif char < aStr[0] or char > aStr[-1]:
        # print(aStr[0], aStr[-1])               # for debug
        # print("2")                             # for debug
        return False
    elif char < aStr[cp]:
        return isIn(char, aStr[:cp])
        # print(aStr[:cp])                       # for debug
    else: # char > aStr[cp]
        return isIn(char, aStr[cp:])
        # print(aStr[:cp])                       # for debug

c = 'b'        # can change c and s for test
s = 'abcdef'
if isIn(c,s):
    print("found")
else:
    print("Not found")
