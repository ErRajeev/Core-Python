#Find Factorial of Number.

# def factorial():
#     n = int(input("Enter A Number...\n"))
#     i = 1
#     fact = 1
#     while i <= n:
#         fact = fact * i
#         i += 1
#     print("Factorial of", n, "is : ", fact)
# factorial()


# Generate Febnache Serios.

# def Feb():
#     len = int(input("Enter a Length.\n"))
#     a = 0
#     c = 0
#     b = 1
#     i = 0
#     while i <= len:
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c
#         i += 1
# Feb()



# Find Reverce of a String

# def Rev():
#     name = input("Enter a String..\n")
#     print(name[ : : -1])
# Rev()

# def Rev():
#     name = input("Enter A String..\n")
#     rever = ""
#     for i in name:
#         rever = i + rever
#     print(rever)
# Rev()

# def Rev():
#     stri = input("Enter a String For Swap..\n")
#     leng = len(stri)
#     i = 0
#     j = leng - 1
#     while i < j:
#         temp = stri[i]
#         stri[i] = stri[j]
#         stri[j] = temp
#         i += 1
#         j -= 1
# Rev()



# Find String is Pelindrome Or not

# def Checkstr():
#     name = input("Enter a String..\n")
#     rev = name[::-1]
#     if name == rev:
#         print("String Is Pelindrome")
#     else:
#         print("String is Not Penlindrome")
# Checkstr()




# Find Comman latter in a string

# def Find():
#     n = input("Enter a String..\n")
#     ch = input("Enter Search latter\n")
#     print(n.count(ch))
# Find()

# def Find():
#     n1 = input("Ente first String...\n")
#     n2 = input("Enter Secont String..\n")
#     comm= []
#     for item in n1:
#         if item in n2:
#             comm.append(item)
#     print(comm)
# Find()




#Avrage in a list

# def Avg():
#     li1 = [2, 4, 6, 8, 10]
#     c = len(li1)
#     tot = 0
#     for item in li1:
#         tot +=  item
#     avg = tot / c
#     print(avg)
# Avg()


# Print Odd Even Seperat In list

def Eve():
    # n = int(input("Enter Number of Element"))
    # li1 = list()
    # ele = int(input("Enter a Element..\n"))
    # for i in range(0, n):
    #     li1.append(ele)
    li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    od = []
    ev = []
    for item in li1:
        if item % 2 == 0:
            ev.append(item)
        else:
            od.append(item)
    print("Odd List is = ", od, "Even list is = ", ev)
Eve()


# defrence between two list
#
# li1 = ["Rajeev", "Aman", "Shubham", "Puja"]
# li2 = ["Rajeev", "Aman", "Shubham", "Shyam"]
# def Diff(li1, li2):
#     diffrence = []
#     for item in li1:
#         if item not in li2:
#             diffrence.append(item)
#     for item in li2:
#         if item not in li1:
#             diffrence.append(item)
#     print(diffrence)
# Diff()
















#
# def Rev():
#     n = input("Enter a String\n")
#     i = len(n) - 1
#     revstr = ""
#     while i >= 0:
#         revstr = revstr + n[i]
#         i -= 1
#     print(revstr)
# Rev()





