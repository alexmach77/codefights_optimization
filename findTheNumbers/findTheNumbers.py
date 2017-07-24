def findTheNumbers(a):
    mydict={}
    for i,ele in enumerate(a):
        if ele not in mydict: mydict[ele] = list()
        mydict[ele].append(i)
        if len(mydict[ele])==2:
            del mydict[ele]
    return sorted(list(mydict.keys()))

if __name__ == '__main__':
    a = [1, 3, 5, 6, 1, 4, 3, 6]
    print findTheNumbers(a)
