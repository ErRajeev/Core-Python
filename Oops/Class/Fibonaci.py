class Fibonaci:
    def __init__(self, n):
        self.n = n

    def printFib(self):
        a = 0
        b = 1
        for i in range(0, self.n):
             print(a)
             temp = a + b
             a = b
             b = temp

if __name__ == "__main__":
    n = int(input("Enter a Number\n"))
    obj = Fibonaci(n)
    obj.printFib()
