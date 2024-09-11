class Prime:
    def __init__(self, n):
        self.n = n

    def check(self):
        if self.n > 1:
            for i in range(2, self.n):
                if (self.n % i) == 0:
                    return False
                else:
                    return True
        else:
            return False


if __name__ == "__main__":
    n = int(input("Enter a Number"))
    ob = Prime(n)
    res = ob.check()
    print(res)
