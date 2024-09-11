class OddEven:
    def __init__(self, n):
        self.n = n

    def check(self):
        if (self.n % 2 == 0):
            print("Evan Number")
        else:
            print("Odd Number")

if __name__ == "__main__":
    n = int(input("Enter a Number\n"))
    ob = OddEven(n)
    ob.check()
