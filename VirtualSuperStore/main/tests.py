list1 = [1,2,3,41]
A = iter(list1)

def generator(a):
    x = a[1]
    a = a[1:]
    yield print(x+1)
    return print(x+1)

generator(list1)