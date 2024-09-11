# f = lambda n : n*n
# res = f(int(input("Enter a number")))
# print(res)


# f = lambda n : 'Even' if n%2==0 else 'Odd'
# res = f((int(input("Enter a number"))))
# print(res)

print((lambda n : 'even' if n % 2 == 0 else 'odd')(int(input("Enter a number"))))