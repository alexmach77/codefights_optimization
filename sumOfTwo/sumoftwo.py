#Goal: Find the most efficient way to check if two lists share any element:
def sumOfTwo(a, b, v):
    return bool(set(a) & set([v-ele for ele in b]))

if __name__ == '__main__':
    import bisect
    a = [1, 2, 3]
    b = [10, 20, 30, 40]
    v = 42
    print sumOfTwo(a, b, v)
