def fibonacci(n):
    """
    Generate the nth Fibonacci number.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Test the program
for i in range(1, 100):
    print(fibonacci(i))