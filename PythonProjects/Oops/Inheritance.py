class Stu:
    def __init__(self, n, a):
        self.na = n
        self.ag = a
    def name(self):
        print("Class a")
        print(self.na, self.ag)
    def age(self):
        print(28)

class New(Stu):
    def oth(self):
        print("Cass B")

# st1 = Stu("Aman", 25)
ob1 = New("Aman", 25)
ob1.name()