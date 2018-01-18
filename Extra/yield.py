def func1():
    a = 0
    while True:
        a += 1
        return a

def func2():
    a = 0
    while True:
        a += 1
        #print(a)
        yield a

f1 = func1()
f2 = func2()

print f1
print f2
