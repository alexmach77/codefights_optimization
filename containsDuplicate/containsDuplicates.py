def containsDuplicate(a):
    if len(a)==len(set(a)):
        return False
    else:
        return True

if __name__ == '__main__':
    a = [1, 2, 3, 1]
    print(containsDuplicate(a))
