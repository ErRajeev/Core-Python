class Student:
    school = "K.R.H.S"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    @classmethod
    def info(cls):
        return cls.school
    # @staticmethod
    # def Factorial():
    #     return ()
    #
Rajeev = Student(98,86,89)
Aman = Student(89,88,83)

print(Rajeev.avg())
print(Student.info())
