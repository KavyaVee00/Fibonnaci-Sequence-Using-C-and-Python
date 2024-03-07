import time
import sys

sys.setrecursionlimit(1000000)  

def fibonacci_iterative(n):
    """
    Solves the Fibonacci series iteratively.
    Args:
        n (int): The index of the Fibonacci series.

    Returns:
        list: A list containing tuples of Fibonacci numbers, number of operations, and time taken for each index.
    """
    result = []
    for i in range(1, n + 1):
        ops = 0
        start_time = time.time()
        if i <= 0:
            fib = 0
        elif i == 1:
            fib = 1
        else:
            a, b = 0, 1
            for _ in range(2, i + 1):
                a, b = b, a + b
                ops += 1
            fib = b
        end_time = time.time()
        result.append((fib, ops, end_time - start_time))
    return result

def fibonacci_recursive(n):
    """
    Solves the Fibonacci series recursively.
    Args:
        n (int): The index of the Fibonacci series.

    Returns:
        list: A list containing tuples of Fibonacci numbers, number of operations, and time taken for each index.
    """
    def fib(n, ops):
        if n <= 0:
            return 0, ops, 0
        elif n == 1:
            return 1, ops, 0
        else:
            start_time = time.time()
            ops += 1
            fib1, ops, _ = fib(n - 1, ops)
            fib2, ops, _ = fib(n - 2, ops)
            end_time = time.time()
            return fib1 + fib2, ops, end_time - start_time
    result = []
    for i in range(1, n + 1):
        result.append(fib(i, 0))
    return result

def fibonacci_dynamic_programming(n):
    """
    Solves the Fibonacci series using dynamic programming.
    Args:
        n (int): The index of the Fibonacci series.

    Returns:
        list: A list containing tuples of Fibonacci numbers, number of operations, and time taken for each index.
    """
    result = []
    for i in range(1, n + 1):
        ops = 0
        start_time = time.time()
        if i <= 0:
            fib = 0
        elif i == 1:
            fib = 1
        else:
            fib_values = [0] * (i + 1)
            fib_values[1] = 1
            for j in range(2, i + 1):
                fib_values[j] = fib_values[j - 1] + fib_values[j - 2]
                ops += 1
            fib = fib_values[-1]
        end_time = time.time()
        result.append((fib, ops, end_time - start_time))
    return result

def measure_algorithm(func, n):
    """
    Measures the execution time and number of operations for a given Fibonacci algorithm.
    Args:
        func (function): The Fibonacci function to measure.
        n (int): The index of the Fibonacci series.

    Returns:
        None
    """
    if func == fibonacci_iterative:
        approach = "Iterative approach"
    elif func == fibonacci_recursive:
        approach = "Recursive approach"
    elif func == fibonacci_dynamic_programming:
        approach = "Dynamic programming approach"
    
    print(approach)
    results = func(n)
    for i, (fib, ops, time_taken) in enumerate(results, start=1):
        print(f"Fibonacci({i}) = {fib}")
        print(f"Operations: {ops}")
        print(f"Time: {time_taken} seconds")
        print()

def main():
    """
    Main function to execute the Fibonacci solver.
    """
    n = int(input("Enter the value of N for Fibonacci Series: "))
    print()

    print("Choose the approach:")
    print("1. Iterative")
    print("2. Recursive")
    print("3. Dynamic programming")
    approach_choice = int(input("Enter your choice: "))

    if approach_choice == 1:
        measure_algorithm(fibonacci_iterative, n)
    elif approach_choice == 2:
        measure_algorithm(fibonacci_recursive, n)
    elif approach_choice == 3:
        measure_algorithm(fibonacci_dynamic_programming, n)
    else:
        print("Invalid choice. Please choose a number between 1 and 3.")

if __name__ == "__main__":
    main()

