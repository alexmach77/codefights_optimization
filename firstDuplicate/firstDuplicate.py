def firstDuplicate(a):
    b=[]
    mydict={}
    for i,ele in enumerate(a):
        if ele in mydict:
            return ele
        else:
            mydict[ele]=i
    else: return -1

'''
if key in list: complexity O(N) since u iterate through the whole list
if key in dict: complexity O(1), because dict implements the "in" function by: by hashing the value and looking up the hash;
'''


if __name__ == '__main__':
    a=[2,3,3,1,5,2]
    print firstDuplicate(a)