def x1():
    global x
    x = 6

def x2():
    global x
    x = x+1
    print x

x = 5
x1()
x2()