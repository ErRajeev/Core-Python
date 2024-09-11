def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1)+fib(n-2))


x = int(input("Enter a number:"))
for i in range(x+1):
    print(fib(i))

5

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


n = int(input("Enter a Number\n"))
print(fact(n))
