def generate_fibonacci(n):
    if n==1:
        return 1
    fibonacci_series = [0, 1]  # Initialize the series with the first two numbers

    while len(fibonacci_series) < n:
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_number)

    return fibonacci_series

# Input: Number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_numbers = generate_fibonacci(n)
    print(f"The first {n} Fibonacci numbers are:")
    print(fibonacci_numbers)
