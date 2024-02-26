# Midterm p1: Report on Analysis of Fibonacci  Series
* **Author**: Kavvya Veeramony
* **GitHub Repo**: [linke to github repo with this report]
* **Semester**: Spring 2024
* **Languages Used**: c, Java 

## Overview
This report focuses on comparing the performance of different implementations of the Fibonacci series algorithm. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. It usually begins with 0 and 1, resulting in 0, 1, 1, 2, 3, 5, 8, and so forth. Each subsequent number is found by adding the two numbers before it. The goal is to analyze the time complexity and space complexity of three different approaches: iterative, recursive, and dynamic programming.

A typical Fibonacci series looks like this:

0, 1, 1, 2, 3, 5, 8, 13, 21, ...


The sequence is defined by the recurrence relation:
```
F(n) = F(n-1) + F(n-2)
```
where F(0) = 0 and F(1) = 1.


Common Approaches:

The table below summarizes the Big O complexity and space usage of each version:

|     Version   | Second Header | Third Header |    
| ------------- | ------------- | ------------ |
| Iterative     | O(n)          | O(1)         |
| Recursive     | O(2^n)        | O(n)
| Dynamic Programming| O(n)     |  O(n)        |


Iterative Approach:

To calculate Fibonacci numbers iteratively, we start with the first two numbers, 0 and 1.
Then, we proceed to compute the next Fibonacci number by adding the previous two.
We repeat this process until we reach the desired position in the sequence.
This method is quite straightforward and efficient, as it only requires going through the sequence once, making it a preferred choice for many.

Recursive Approach:

The recursive method involves defining a function that calls itself to calculate Fibonacci numbers.
It starts with base cases for the first two Fibonacci numbers and recursively computes subsequent numbers.
However, this approach tends to be less efficient due to redundant calculations, especially for larger numbers, making it slower and less practical.

Dynamic Programming Approach:

Dynamic programming offers an solution by storing previously computed Fibonacci numbers.
We utilize memoization or tabulation to avoid recomputing the same Fibonacci numbers.
By storing the results, we can quickly access them when needed which significantly improves efficiencye for larger Fibonacci sequences.


I decided to go with Python as my second language because of its widespread use and its powerful features. Python's simplicity and readability make it an excellent choice for solving problems like the Fibonacci sequence. Plus, I wanted to challenge myself by delving into a language that complements my knowledge of C. It's a great way to broaden my programming skills and explore different programming paradigms. 

## Empirical Data & Discussion 
For the empirical analysis, I ran each implementation with various input values of n and recorded the execution times. I also compared the number of operations performed by each algorithm for different values of n.

The operations count for C code: 

#### Operations Count 
| **N** | **Iterative** | **Dynamic Programming** | **Recursive** |
|-------|---------------:|-------------------------:|---------------:|
| 1     | 0             | 0                       | 0             |
| 2     | 2             | 1                       | 2             |
| 3     | 4             | 2                       | 4             |
| 4     | 6            | 6                       | 8            |
| 5     | 8            | 8                      | 14            |
| 6     | 10            | 10                      | 24            |
| 7     | 12            | 12                      | 40           |
| 8     | 14            | 14                      | 66           |
| 9     | 16            | 16                      | 108           |
| 10    | 18            | 18                      | 176          |
| 11    | 20            | 20                      | 286          |
| 12    | 22            | 22                      | 464          |
| 13    | 24            | 24                      | 752          |
| 14    | 26           | 26                      | 1218         |
| 15    | 28           | 28                     | 1972         |
| 16    | 30           | 30                     | 3192         |
| 17    | 32           | 32                     | 5166        |
| 18    | 34           | 34                     | 8360        |
| 19    | 36          | 36                     | 13528        |
| 20    | 38           | 38                     | 21890       |
| 21    | 40           | 40                     | 35420       |
| 22    | 42           | 42                     | 57312       |
| 23    | 44           | 44                     | 92734       |
| 24    | 46           | 46                     | 150048     |
| 25    | 48           | 48                     | 242784     |
| 26    | 50           | 50                     | 392834      |
| 27    | 52           | 522                     | 635620     |
| 28    | 54           | 54                     | 1028456     |





The data we gathered by running the code matches what we expected based on our understanding of the algorithms. The iterative and dynamic programming methods consistently show low timings, which makes sense since they're designed to be efficient, especially for larger values of n.

On the other hand, the recursive approach takes significantly longer as n increases. This isn't surprising given its exponential time complexity. Essentially, as n grows, the recursive approach has to redo a lot of calculations, leading to longer execution times compared to the other methods.

Apart from the algorithm itself, there are other factors that can affect runtime. Things like the speed of your computer's processor, how much memory is available, and even how the code is compiled can all have an impact. Additionally, the operating system's tasks like scheduling can also affect how quickly your code runs.



## Language Analysis


### Language 1: C
So in order to satisfy all the requirements in the code, I needed a clear understanding of the iterative, recursive, and dynamic programming algorithms for generating Fibonacci numbers. This involved breaking down each algorithm into its fundamental steps and understanding how they work. 
  * For the iterative approach, I grasped the concept of using a loop to generate Fibonacci numbers iteratively by summing the previous two numbers.
  * In the recursive approach, I understood the concept of breaking down the problem into smaller subproblems by defining the Fibonacci sequence recursively.
  * For dynamic programming, I learned about using an array to store previously computed Fibonacci numbers to avoid redundant calculations.

For the iterative approach, I implemented a loop that iterated from 2 to n, updating Fibonacci numbers iteratively by adding the previous two numbers. The main concern here was to ensure that the loop correctly updated the values without missing any intermediate steps. Additionally, I had to track the number of operations performed during the calculation.

```c
ull fibonacci_iterative(int n, ull *ops)
{
    ull a = 0, b = 1, c, i;
    if (n == 0)
        return a;
    for (i = 2; i <= n; i++)
    {
        (*ops)++;
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}
```

For dynamic programming, I implemented a function that stored previously calculated Fibonacci numbers in an array to avoid redundant calculations. Memory management and ensuring correct indexing within the array were key considerations. 

```c
ull fibonacci_dp(int n, ull *ops)
{
    ull fib[MAX];
    fib[0] = 0;
    fib[1] = 1;
    for (int i = 2; i <= n; i++)
    {
        (*ops)++;
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    return fib[n];
}
```

The recursive approach posed challenges due to its exponential time complexity, especially for large values of n. Ensuring proper termination conditions and tracking the number of operations became crucial to understanding the efficiency of the algorithm.

```c
ull fibonacci_recursive(int n, ull *ops)
{
    if (n <= 1) {
        return n;
    }

    *ops += 1; // Counting one operation for the addition
    return fibonacci_recursive(n - 1, ops) + fibonacci_recursive(n - 2, ops);
}
```

One roadblock that I had faced was that in my original code, the number of operations for each of the approaches was abnormally high. 

For example, this is some of the output from that code: 
```c
Kavyas-MacBook-Air:Midterm-1 kavyav$ ./fibonacci 28 1
Iterative approach
Fibonacci(1) = 1
Operations: 0
Time: 0.000001 seconds


Iterative approach
Fibonacci(2) = 1
Operations: 2
Time: 0.000000 seconds


Iterative approach
Fibonacci(3) = 2
Operations: 6
Time: 0.000000 seconds


Iterative approach
Fibonacci(4) = 3
Operations: 12
Time: 0.000000 seconds


Iterative approach
Fibonacci(5) = 5
Operations: 20
Time: 0.000001 seconds


Iterative approach
Fibonacci(6) = 8
Operations: 30
Time: 0.000000 seconds


Iterative approach
Fibonacci(7) = 13
Operations: 42
Time: 0.000001 seconds


Iterative approach
Fibonacci(8) = 21
Operations: 56
Time: 0.000001 seconds


Iterative approach
Fibonacci(9) = 34
Operations: 72
Time: 0.000000 seconds


Iterative approach
Fibonacci(10) = 55
Operations: 90
Time: 0.000000 seconds


Iterative approach
Fibonacci(11) = 89
Operations: 110
Time: 0.000000 seconds


Iterative approach
Fibonacci(12) = 144
Operations: 132
Time: 0.000000 seconds


Iterative approach
Fibonacci(13) = 233
Operations: 156
Time: 0.000000 seconds


Iterative approach
Fibonacci(14) = 377
Operations: 182
Time: 0.000000 seconds


Iterative approach
Fibonacci(15) = 610
Operations: 210
Time: 0.000000 seconds


Iterative approach
Fibonacci(16) = 987
Operations: 240
Time: 0.000000 seconds


Iterative approach
Fibonacci(17) = 1597
Operations: 272
Time: 0.000001 seconds


Iterative approach
Fibonacci(18) = 2584
Operations: 306
Time: 0.000000 seconds


Iterative approach
Fibonacci(19) = 4181
Operations: 342
Time: 0.000000 seconds


Iterative approach
Fibonacci(20) = 6765
Operations: 380
Time: 0.000000 seconds


Iterative approach
Fibonacci(21) = 10946
Operations: 420
Time: 0.000000 seconds


Iterative approach
Fibonacci(22) = 17711
Operations: 462
Time: 0.000000 seconds


Iterative approach
Fibonacci(23) = 28657
Operations: 506
Time: 0.000000 seconds


Iterative approach
Fibonacci(24) = 46368
Operations: 552
Time: 0.000000 seconds


Iterative approach
Fibonacci(25) = 75025
Operations: 600
Time: 0.000001 seconds


Iterative approach
Fibonacci(26) = 121393
Operations: 650
Time: 0.000000 seconds


Iterative approach
Fibonacci(27) = 196418
Operations: 702
Time: 0.000000 seconds


Iterative approach
Fibonacci(28) = 317811
Operations: 756
Time: 0.000001 seconds
```

The number of operations were abnormally large. After looking more closely at my code, I realized that noticed I'm using another loop for (int i = 1; i <= n; i++), but for each function, I already have the for (int i = 1; i <= n; i++) loop, so essentially, I'm duplicating it.
```c
for this part of code for (int i = 1; i <= n; i++)
    {
        switch (type)
        {
        case 1:
            printf("Iterative approach\n");
            time = time_function(fibonacci_iterative, i, &ops);
            printf("Fibonacci(%d) = %llu\n", i, fibonacci_iterative(i, &ops));
            printf("Operations: %llu\n", ops);
            printf("Time: %f seconds\n", time);
            break;
        case 2:
            printf("Recursive approach\n");
            time = time_function(fibonacci_recursive, i, &ops);
            printf("Fibonacci(%d) = %llu\n", i, fibonacci_recursive(i, &ops));
            printf("Operations: %llu\n", ops);
            printf("Time: %f seconds\n", time);
            break;
        case 3:
            printf("Dynamic programming approach\n");
            time = time_function(fibonacci_dp, i, &ops);
            printf("Fibonacci(%d) = %llu\n", i, fibonacci_dp(i, &ops));
            printf("Operations: %llu\n", ops);
            printf("Time: %f seconds\n", time);
            break;
        }
        printf("\n");
    }
```
So essentially it was calculating
0 1
0 1 2
0 1 2 3
Etc all the way  

I updated my code so that it would basically reset the operations to 0 each time. 

```c
for (int i = 1; i <= n; i++)
    {
        ull ops = 0;
        double time;
        switch (type)
        {

```

Overall, implementing the Fibonacci series calculation in C required attention to algorithmic efficiency, memory management, and accurate timing measurement to evaluate the performance of different approaches.

### Language 2: PYTHON
Implementing the Fibonacci series solver in Python was straightforward thanks to several language features and libraries.

Modules: The code starts by importing the time and sys modules. These are used for measuring execution time and adjusting the recursion limit, respectively. 

Tuple Returns: Python's ability to return tuples from functions was useful for bundling the nth Fibonacci number, the number of operations, and the time taken into a single return value. This streamlined the code and made it more readable. 

```c
def fibonacci_recursive(n):
    """
    Solves the Fibonacci series recursively.
    Args:
        n (int): The index of the Fibonacci series.

    Returns:
        tuple: A tuple containing the nth Fibonacci number, the number of operations, and the time taken.
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
    return fib(n, 0)
```
For example, the fibonacci_recursive function returns a tuple containing the nth Fibonacci number, the number of operations, and the time taken. This allows for concise and readable code, as all relevant information is bundled together in a single return value.

Another feature that I found to be very usueful was the Recursion Limit Adjustment. The Python's sys.setrecursionlimit()function enabled adjusting the recursion limit, allowing for deeper recursion in the recursive solution without encountering stack overflow errors. However a concern with that was while Python's recursion depth is typically limited to 1000 by default, increasing the recursion limit using sys.setrecursionlimit() was necessary to accommodate larger values of N for the recursive solution. I found that adjusting the recursion limit should be done with caution to avoid crashing the program due to excessive memory usage.

Functions: 
Iterative Solution: The fibonacci_iterative function calculates Fibonacci numbers iteratively using a loop. This approach is straightforward and efficient, as it doesn't rely on recursion and doesn't have the risk of hitting the recursion limit. 
```c
ull fibonacci_iterative(int n, ull *ops)
{
    ull a = 0, b = 1, c, i;
    if (n == 0)
        return a;
    for (i = 2; i <= n; i++)
    {
        (*ops)++;
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}
```

Recursive Solution: The fibonacci_recursive function provides a recursive solution to calculate Fibonacci numbers. It uses a nested function fib() to handle recursive calls. While elegant, recursive solutions can lead to stack overflow errors for large inputs due to Python's default recursion limit. Hence, the recursion limit is adjusted using sys.setrecursionlimit().
```c
def fibonacci_recursive(n):
    """
    Solves the Fibonacci series recursively.
    Args:
        n (int): The index of the Fibonacci series.

    Returns:
        tuple: A tuple containing the nth Fibonacci number, the number of operations, and the time taken.
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
    return fib(n, 0)
```
Dynamic Programming Solution: The fibonacci_dynamic_programming function implements the Fibonacci series using dynamic programming. It uses a list to store intermediate results, avoiding redundant calculations. However, memory usage could be a concern for large inputs, as dynamic programming solutions require storing all intermediate results.
```c
def fibonacci_dynamic_programming(n):
    """
    Solves the Fibonacci series using dynamic programming.
    Args:
        n (int): The index of the Fibonacci series.

    Returns:
        tuple: A tuple containing the nth Fibonacci number, the number of operations, and the time taken.
    """
    if n <= 0:
        return 0, 0, 0
    elif n == 1:
        return 1, 0, 0
    else:
        ops = 0
        start_time = time.time()
        fib = [0] * (n + 1)
        fib[1] = 1
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
            ops += 1
        end_time = time.time()
        return fib[n], ops, end_time - start_time
```

### Comparison and Discussion Between Experiences


## Conclusions / Reflection

## References

