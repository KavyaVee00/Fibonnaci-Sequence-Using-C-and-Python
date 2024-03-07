import csv
import sys
import time

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
        result.append((i, fib, ops, end_time - start_time))
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
        result.append((i,) + fib(i, 0))
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
        result.append((i, fib, ops, end_time - start_time))
    return result

def write_csv(data, filename):
    """
    Writes the data to a CSV file.
    Args:
        data (list): List of tuples containing data to write.
        filename (str): Name of the CSV file.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["N", "Iterative", "Dynamic Programming", "Recursive"])
        for row in data:
            writer.writerow(row)

def main():
    """
    Main function to execute the Fibonacci solver and print results.
    """
    n = int(input("Enter the value of N for Fibonacci Series: "))
    print()

    iterative_results = fibonacci_iterative(n)
    recursive_results = fibonacci_recursive(n)
    dynamic_results = fibonacci_dynamic_programming(n)

    table_data = []
    for i in range(n):
        table_data.append((iterative_results[i][0], iterative_results[i][3], dynamic_results[i][3], recursive_results[i][3]))

    print("| **N** | **Iterative** | **Dynamic Programming** | **Recursive** |")
    print("|-------|---------------|-------------------------|---------------|")
    for row in table_data:
        print("|", " | ".join(map(str, row)), "|")

    write_csv(table_data, "fibonacci_timings.csv")

if __name__ == "__main__":
    main()
