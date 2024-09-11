try:
    a = int(input("Enter First number "))
    b = int(input("Enter Second Number "))
    a = 5
    b = 0
    c = a/b
except Exception as e:
    print("Error ",e)

finally:
    print("This is Python programming")
