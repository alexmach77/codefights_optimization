def rotateImage(matrix):
    from collections import defaultdict
    mydict = defaultdict(list)
    n=len(matrix)

    for lista in reversed(matrix):
        print(lista)
        for i in range(0,n):
            mydict[i].append(lista[i])

    return [row for row in mydict.values()]

if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print(rotateImage(matrix))
