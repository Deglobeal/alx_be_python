# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        # Static method to add two numbers
        return a + b

    @classmethod
    def multiply(cls, a, b):
        # Class method to multiply two numbers and print class attribute
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Example usage of the Calculator class
if __name__ == "__main__":
    # Using the static method to add two numbers
    sum_result = Calculator.add(5, 10)  # Updated to 5 + 10 = 15
    print(f"The sum is: {sum_result}")

    # Using the class method to multiply two numbers
    product_result = Calculator.multiply(5, 10)  # Updated to 5 * 10 = 50
    print(f"The product is: {product_result}")
