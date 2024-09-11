class Check:
    def __init__(self, n):
        self.n = n

    def fib(self, n):
        if n <= 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)


nterms = int(input("How many terms? "))
obj = Check(nterms)
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(obj.fib(i))