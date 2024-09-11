# simple function
def first():
    print("Rajeev Ranjan")

# passing argument
def second(a):
    x = 5
    print(a+x)

# return value
def third():
    n = int(input("Enter A Number\n"))
    fact = 1
    while(n!=0):
        fact = fact*n
        n = n-1
    return fact

# function with list as parameter and list as return value
def forth(p):
    for i in p:
        print(i)
    return [i for i in p]

# function with tuple as parameter and tuple as return value
def fifth(p):
    for i in p:
        print(i)
    return [i for i in p]


# function with dictionary as parameter and dictionary as return value
def sixth(dic):
    x = print(len(dic))
    y = print(type(dic))
    return x, y


# function with return type
def seven():
    x = int(input("Enter a number for chek Even or Odd"))
    if x % 2 == 0:
        return ("Even")
    else:
        return ("Odd")

# function with return multiple values
def eight():
    x = "22mcr087"
    y = "Rajeev Ranjan"
    return x, y

print("1 : Simple function\n2 : Passing Argument\n3 : Return Value\n4 : Function with list as Parameter and list as return value")
print("5 : Function with Tuple as Parameter and Tuple as return value")
print("6 : Function with dictionary as Parameter and dictionary as return value\n8 : Function with return type as functions\n9 : EXIT")
print("-------------------------------------------\n")

def main():
    ch = int(input("\nEnter your Choice :\n",))
    if ch == 1:
        first()
        main()
    elif ch == 2:
        second(3)
        main()
    elif ch == 3:
        print("Factorial = ",third())
        main()
    elif ch == 4:
        list = ["Rajeev", "Pooja", "Aman"]
        print(forth(list),"\n")
        main()
    elif ch == 5:
        tupple = ("Rajeev", "Pooja", "Aman")
        print(fifth(tupple))
        main()
    elif ch == 6:
        dictionary = {"Roll no": "22mcr087", "Name": "Rajeev Ranjan", "DOB": "10/02/2001"}
        print(sixth(dictionary))
        main()
    elif ch == 7:
        print(seven(),"\n")
        main()
    elif ch == 8:
        xxx = eight()
        print("Roll = {a} Name = {b}".format(a = xxx[0], b = xxx[1]))
        main()
    else:
        exit(0)
main()