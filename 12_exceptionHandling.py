def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both arguments must be numbers."
    else:
        return f"The result is {result}"
    finally:
        print("Execution completed.")

# Test the function
print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, 'a'))