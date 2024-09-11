class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


    def details(self):
        print(self.name, self.roll)

    class Laptop:
        def __init__(self, brand, ram, cpu):
            self.brand = brand
            self.ram = ram
            self.cpu = cpu

        def conf(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Rajeev', 8)
s1.details()
c = Student.Laptop('Hp', '8Gb', 'i7')
c.conf()