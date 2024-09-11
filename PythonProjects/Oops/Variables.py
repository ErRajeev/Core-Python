class Car:
    wheel = 4
    def __init__(self):
        self.com = "BMW"
        self.mil = 100

c1 = Car()
c2 = Car()
c2.mil = 120
print("1st Car -", c1.com, c1.mil, c1.wheel)
print("2nd Car -", c2.com, c2.mil, c2.wheel)