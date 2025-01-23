"""this program is a practices program for working on staticmethod  """ 
"""creating a static_method for maths calculation of two or more numbers! """

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "can't divide by zero"
        return a / b

print(MathUtils.add(5,3))
print(MathUtils.subtract(5,3))
print(MathUtils.multiply(5,3))
print(MathUtils.divide(5,3))
print(MathUtils.divide(5,0))