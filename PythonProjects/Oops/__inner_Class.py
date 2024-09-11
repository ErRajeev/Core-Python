class Student:
    def __init__(self, rol, name, add):
        self.roll = rol
        self.ex = "-"
        self.name = name
        self.add = add

        self.Aman_lap = Student.Laptop()
        self.Rajeev_lap = Student.Laptop()

    def details(self):
        print(self.roll, self.ex, self.name, self.add)
        self.Aman_lap.conf()

    class Laptop:
        def __init__(self):
            self.brand = "Hp"
            self.cpu = "i5, 8th Gen"
            self.ram = "8Gb"
        def conf(self):
            print(end="\t")
            print(self.brand, self.cpu, self.ram)


Aman = Student(1, "Aman Raj", "Banuchhapar, Bettiah, Bihar")
Rajeev = Student(2, "Rajeev Ranjan", "Chhawni, Bettiah, Bihar")

Aman.details()
# Aman.Aman_lap.conf()
# lap1 = Aman.Aman_lap.conf()
Rajeev.details()
# Rajeev.Rajeev_lap.conf()
# lap2 = Rajeev.Rajeev_lap()


