class Computer:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("This The Computer")

    def process(self):
        print(self.a+self.b)
        # print("i5 8Gb 512Gb")


hp = Computer()
# sam = Computer()
hp.process(2, 5)
# sam.process()
