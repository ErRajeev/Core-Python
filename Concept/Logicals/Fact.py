def Fact(n):
    if n <= 1:
        return 1
    else:
        return n * Fact(n-1)


n = int(input("Enter a number"))
print(Fact(n))