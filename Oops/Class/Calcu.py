class Calculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2

    def sub(self):
        return self.n1 - self.n2

    def mult(self):
        return self.n1 * self.n2

    def div(self):
        return self.n1 / self.n2

    def mod(self):
        return self.n1 % self.n2

    def decision(self, userDecision):
        if userDecision == "+":
            return self.add()
        elif userDecision == "-":
            return self.sub()
        elif userDecision == "*":
            return self.mult()
        elif userDecision == "/":
            return self.div()
        elif userDecision == "%":
            return self.mod()


if __name__ == "__main__":
    while (1):
        userInput = input("Enter your Expression\n")
        userInput = userInput.split(" ")
        n1 = int(userInput[0])
        userDecision = (userInput[1])
        n2 = int(userInput[-1])
        obj = Calculator(n1, n2)
        res = obj.decision(userDecision)
        print(n1, userDecision, n2, '=', res)

        ch = input("\nDo you want more Calculation...??\nY = Yes N = No\n")
        if ch.lower()[0] == 'y':
            continue
        else:
            break
