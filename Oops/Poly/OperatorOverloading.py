class Demo:
    def __init__(self) -> None:
        pass

    def mult(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            return a*b*c
        elif a != None and b != None and c != None:
            return a*b
        elif a != None:
            return a
        else:
            print("Enter atlist one Number")


class Demo2:
    def __init__(self) -> None:
        pass

    def mult(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            return a*b*c
        elif a != None and b != None and c != None:
            return a*b
        elif a != None:
            return a
        else:
            print("Enter atlist one Number")


obj = Demo2()
print(obj.mult(3, 8, 1))
