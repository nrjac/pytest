def fib(n):
    global counter
    if (n == 0 or n == 1):
        counter=counter+1
        return 1
    else:
        counter=counter+1
        return fib(n-1) + fib(n-2)
def countfib(n):
    global counter
    counter = 0
    fib(5);
    global count
    count=counter
    counter = 0
    return count
counter=0
count=0
print fib(5)
count=countfib(5)
print count