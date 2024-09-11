# class Computer:
#     def __init__(self, cpu, ram, gpu):
#         self.cpu = cpu
#         self.ram = ram
#         self.gpu = gpu
#     def config(self):
#         print("Configation", self.cpu, self.ram, self.gpu)
# hp = Computer("i5", "16Gb", "1080Ti")
# hp.config()


# class Computer:
#     def __init__(self):
#         print("This is Hp Laptop")
# hp = Computer()


# class Student:
#     def __init__(self):
#         self.name = "Rajeev Ranjan"
#         self.age = 22
#
# ob1 = Student()
# ob2 = Student()
# print(ob1.name, ob1.age)
# print(ob2.name, ob1.age)



class Student:
    def __init__(self):
        self.name = "Rajeev Ranjan"
        self.age = 22

ob1 = Student()
ob2 = Student()
ob2.name = "Aman Tiwari"
ob2.age = 18
print(ob1.name, ob1.age)
print(ob2.name, ob1.age)