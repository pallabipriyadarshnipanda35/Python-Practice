class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

# Create an instance of MathOperations
math_ops = MathOperations()

# Call the add method with two arguments
result1 = math_ops.add(10, 20)
print("Sum with two arguments:", result1)

# Call the add method with three arguments
result2 = math_ops.add(10, 20, 30)
print("Sum with three arguments:", result2)