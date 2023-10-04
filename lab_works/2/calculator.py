import math

class Calculator:

    def __init__(self):
        self.first_value = None
        self.operator = None
        self.second_value = None

    def run(self):
        while True:
            try:
                self.input()
                print("The result is {}".format(self.calculate()))

            except Exception as e:
                print(str(e))
            response = str(input("Would you like to continue? Enter 'Y' or 'y' if you do, or anything else if you do "
                                 "not. Your response is "))
            if response.lower() != "y":
                break

    def input(self):
        try:
            self.__init__()
            self.first_value = float(input("Enter the first value: "))
            self.operator = str(input("Enter the operator ['+', '-', '*', '/', '**', '√', '%']: "))
            if self.__is_operator_correct(self.operator):
                if self.operator != "√":
                    self.second_value = float(input("Enter the second value: "))
            else:
                raise RuntimeWarning("The input operator is incorrect")
        except ValueError as e:
            raise type(e)("The format of number is invalid")

    @staticmethod
    def __is_operator_correct(operator):
        valid_operators = ('+', '-', '*', '/', '**', '√', '%')
        return operator in valid_operators

    def calculate(self):
        if self.operator == "+":
            return self.first_value + self.second_value
        elif self.operator == "-":
            return self.first_value - self.second_value
        elif self.operator == "*":
            return self.first_value * self.second_value
        elif self.operator == "/":
            if self.second_value == 0:
                raise ZeroDivisionError("Impossible to divide")
            return self.first_value / self.second_value
        elif self.operator == "**":
            return self.first_value ** self.second_value
        elif self.operator == "√":
            if self.first_value < 0:
                raise ArithmeticError("Number is negative, therefore it is impossible to  calculate the square root")
            return math.sqrt(self.first_value)
        elif self.operator == "%":
            return self.first_value % self.second_value


c = Calculator()
c.run()