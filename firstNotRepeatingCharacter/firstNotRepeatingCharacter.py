from collections import defaultdict


def firstNotRepeatingCharacter(s):

    mydict = defaultdict(int)
    for c in s:
        mydict[c]=mydict[c]+1
    print(mydict)

    for c in s:
        if mydict[c]==1:
            return c
    return '_'


if __name__ == '__main__':
    s = "abacabad"
    print(firstNotRepeatingCharacter(s))