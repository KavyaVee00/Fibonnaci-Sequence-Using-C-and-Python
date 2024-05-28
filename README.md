# Midterm p1: Report on Analysis of Fibonacci  Series
* **Author**: Kavya Veeramony
* **GitHub Repo**:(https://github.com/Sp24-CS5008-Online-Lionelle/midterm-KavyaVee00.git)
* **Semester**: Spring 2024
* **Languages Used**: c, Python

## Overview
This report focuses on comparing the performance of different implementations of the Fibonacci series algorithm using Python and C. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. It usually begins with 0 and 1, resulting in 0, 1, 1, 2, 3, 5, 8, and so forth. Each subsequent number is found by adding the two numbers before it. The goal is to analyze the time complexity and space complexity of three different approaches: iterative, recursive, and dynamic programming.

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

Iterative Approach:
When we calculate Fibonacci numbers iteratively, the number of steps increases steadily as we go higher in the sequence.
For every increase in the Fibonacci index N, we see an additional 2 operations.
This method is pretty straightforward and predictable. Each Fibonacci number takes a fixed number of additions and assignments to compute.

Dynamic Programming Approach:
With dynamic programming, the number of operations remains the same for each N.
This technique stores previously calculated Fibonacci numbers in an array, which means we don't need to redo computations.
So, regardless of how big N gets, the number of operations stays constant. The operation count for both Dynamic and Iterative are the same. 

Recursive Approach:
Here's where things get interesting. The number of operations shoots up really fast as N increases.
This approach involves a lot of repeated recursive calls and recalculations, making it much slower for larger N values.
It's conceptually simple, but it becomes pretty inefficient as N gets bigger.


## Timings for C: 
| **N** | **Iterative** | **Dynamic Programming** | **Recursive** |
|-------|---------------:|-------------------------:|---------------:|
1|0.000004,        |0.000002        |0.000002
2|0.000001         |0.000001       |0.000001
3|0.000000|0.000001|0.000002|
4|0.000001|0.000002|0.000002|
5|0.000002|0.000001|0.000001|
6|0.000001|0.000001|0.000001|
7|0.000002|0.000000,0.000002|
8|0.000001|0.000002|0.000003|
9|0.000002|0.000002|0.000003|
10|0.000001|0.000001|0.000002|
11|0.000000|0.000001|0.000003|
12|0.000001|0.000002|0.000009|
13|0.000002|0.000001|0.000004|
14|0.000002|0.000001|0.000007|
15|0.000002|0.000002|0.000010|
16|0.000001|0.000001|0.000013|
17|0.000001|0.000002|0.000024|
18|0.000000|0.000001|0.000036|
19|0.000001|0.000002|0.000056|
20|0.000001|0.000002|0.000093|
21|0.000000|0.000001|0.000146|
22|0.000000|0.000001|0.000237|
23|0.000001|0.000001|0.000378|
24|0.000002|0.000000|0.000606|
25|0.000002|0.000000|0.000989|
26|0.000002|0.000001|0.001608|
27|0.000001|0.000001|0.002589|
28|0.000000|0.000001|0.004710|
29|0.000002|0.000001|0.007800|
30|0.000001|0.000001|0.011794|
31|0.000002|0.000000|0.019333|
32|0.000002|0.000002|0.030318|
33|0.000001|0.000001|0.050615|
34|0.000002|0.000001|0.081557|
35|0.000001|0.000002|0.121736|
36|0.000001|0.000001|0.192782|
37|0.000002|0.000002|0.324212|
38|0.000001|0.000002|0.515111|
39|0.000001|0.000002|0.824204|
40|0.000001|0.000001|1.327554|
41|0.000002|0.000001|2.123652|
42|0.000001|0.000001|3.442512|
43|0.000003|0.000002|5.588105|
44|0.000002|0.000002|8.827117|
45|0.000002|0.000004|14.268852|
46|0.000002|0.000002|23.197690|
47|0.000002|0.000001|37.692939|
48|0.000002|0.000001|61.184132|
49|0.000001|0.000000|100.433627|
50|0.000002|0.000002|165.314438|

The data we gathered by running the code matches what we expected based on our understanding of the algorithms. The iterative and dynamic programming methods consistently show low timings, which makes sense since they're designed to be efficient, especially for larger values of n. 

- The iterative approach generally shows consistent and low execution times across different values of 'n'.
As 'n' increases, the execution time also increases gradually, but the increase is relatively small and linear.

- The dynamic programming approach also exhibits consistent and relatively low execution times.
Similar to the iterative approach, the dynamic programming approach shows gradual increases in execution time as 'n' increases.
It performs slightly slower than the iterative approach but still maintains reasonable execution times even for larger values of 'n'.

On the other hand, the recursive approach takes significantly longer as n increases. The recursive approach shows significantly higher execution times compared to the iterative and dynamic programming approaches. As 'n' increases, the execution time grows exponentially, leading to much longer processing times for larger values of 'n'.This isn't surprising given its exponential time complexity. Essentially, as n grows, the recursive approach has to redo a lot of calculations, leading to longer execution times compared to the other methods. The recursive approach becomes increasingly inefficient for larger 'n' values due to the repeated computations and function calls.

Apart from the algorithm itself, there are other factors that can affect runtime. Things like the speed of my computer's processor, how much memory is available, and even how the code is compiled can all have an impact. Additionally, the operating system's tasks like scheduling can also affect how quickly your code runs.

Overall, the timings suggest that the iterative and dynamic programming approaches are more efficient for calculating Fibonacci numbers compared to the recursive approach, particularly for larger values of 'n'. The iterative approach is the fastest, followed by dynamic programming, while the recursive approach is the slowest and least efficient, especially for large 'n' values.

## Timings for Python: 

| **N** | **Iterative** | **Dynamic Programming** | **Recursive** |
|-------|---------------|-------------------------|---------------|
| 1 | 1.1920928955078125e-06 | 9.5367431640625e-07 | 0 |
| 2 | 2.1457672119140625e-06 | 1.621246337890625e-05 | 4.0531158447265625e-06 |
| 3 | 9.5367431640625e-07 | 1.0967254638671875e-05 | 2.86102294921875e-06 |
| 4 | 1.1920928955078125e-06 | 1.1205673217773438e-05 | 4.0531158447265625e-06 |
| 5 | 9.5367431640625e-07 | 1.9073486328125e-06 | 5.9604644775390625e-06 |
| 6 | 9.5367431640625e-07 | 9.5367431640625e-07 | 1.2874603271484375e-05 |
| 7 | 1.1920928955078125e-06 | 9.5367431640625e-07 | 2.002716064453125e-05 |
| 8 | 9.5367431640625e-07 | 9.5367431640625e-07 | 3.790855407714844e-05 |
| 9 | 9.5367431640625e-07 | 2.1457672119140625e-06 | 5.412101745605469e-05 |
| 10 | 1.1920928955078125e-06 | 1.0013580322265625e-05 | 6.890296936035156e-05 |
| 11 | 0.0 | 9.5367431640625e-07 | 8.20159912109375e-05 |
| 12 | 1.1920928955078125e-06 | 1.9073486328125e-06 | 0.0001361370086669922 |
| 13 | 9.5367431640625e-07 | 2.1457672119140625e-06 | 0.00039315223693847656 |
| 14 | 7.152557373046875e-07 | 7.867813110351562e-06 | 0.00047206878662109375 |
| 15 | 9.5367431640625e-07 | 1.9073486328125e-06 | 0.0008780956268310547 |
| 16 | 9.5367431640625e-07 | 1.6927719116210938e-05 | 0.0011110305786132812 |
| 17 | 1.1920928955078125e-06 | 2.1457672119140625e-06 | 0.0013952255249023438 |
| 18 | 9.5367431640625e-07 | 1.0967254638671875e-05 | 0.0022592544555664062 |
| 19 | 1.1920928955078125e-06 | 3.0994415283203125e-06 | 0.003718852996826172 |
| 20 | 9.5367431640625e-07 | 8.821487426757812e-06 | 0.006916046142578125 |
| 21 | 1.6689300537109375e-06 | 1.9073486328125e-06 | 0.010946035385131836 |
| 22 | 1.1920928955078125e-06 | 3.0994415283203125e-06 | 0.01690816879272461 |
| 23 | 9.5367431640625e-07 | 2.86102294921875e-06 | 0.03233695030212402 |
| 24 | 2.1457672119140625e-06 | 1.811981201171875e-05 | 0.04691886901855469 |
| 25 | 1.9073486328125e-06 | 2.86102294921875e-06 | 0.07357430458068848 |
| 26 | 2.1457672119140625e-06 | 2.7179718017578125e-05 | 0.12831711769104004 |
| 27 | 1.9073486328125e-06 | 1.8835067749023438e-05 | 0.19426393508911133 |
| 28 | 8.821487426757812e-06 | 4.291534423828125e-06 | 0.3204989433288574 |
| 29 | 3.0994415283203125e-06 | 1.0967254638671875e-05 | 0.5167279243469238 |
| 30 | 4.0531158447265625e-06 | 3.0994415283203125e-06 | 0.848642110824585 |
| 31 | 3.814697265625e-06 | 3.0994415283203125e-06 | 1.340763807296753 |
| 32 | 5.245208740234375e-06 | 1.9073486328125e-05 | 2.3085482120513916 |
| 33 | 3.814697265625e-06 | 4.0531158447265625e-06 | 3.5504071712493896 |
| 34 | 5.245208740234375e-06 | 1.2636184692382812e-05 | 5.970300197601318 |
| 35 | 4.76837158203125e-06 | 4.291534423828125e-06 | 9.4778733253479 |
| 36 | 5.0067901611328125e-06 | 2.09808349609375e-05 | 15.338347911834717 |
| 37 | 2.002716064453125e-05 | 4.0531158447265625e-06 | 24.612709045410156 |
| 38 | 5.0067901611328125e-06 | 4.76837158203125e-06 | 40.01042580604553 |
| 39 | 5.0067901611328125e-06 | 4.0531158447265625e-06 | 64.90412497520447 |
| 40 | 5.0067901611328125e-06 | 2.09808349609375e-05 | 110.56338214874268 |

After examining the practical results from running the code and recording timings for each Fibonacci calculation method, I noticed several key points:

Iterative Approach: The iterative method consistently showed the fastest timings. This wasn't surprising, as it involves a straightforward loop-based calculation, which tends to be efficient.

Dynamic Programming Approach: Timings for the dynamic programming method were generally higher than the iterative approach but lower than the recursive approach. Dynamic programming optimizes calculations by storing previously computed values, reducing redundant work.

Recursive Approach: The recursive method consistently exhibited the slowest timings. This was expected, given that recursion involves repeated function calls and redundant calculations, resulting in slower execution.

Consistency with Expectations: Overall, the runtime data aligned well with my initial analysis, with timings following the anticipated order: iterative < dynamic programming < recursive.

Other Factors Impacting Runtime: Besides the algorithm, I also considered various real-world factors that could influence runtime, such as hardware capabilities, system load, compiler optimizations, input size, language overhead, and cache behavior.

## Comparison of the timings of C and Python: 
When comparing the Python and C timings for calculating Fibonacci numbers, it's pretty clear that C outpaces Python by a long shot. No matter the method—be it Iterative, Dynamic Programming, or Recursive—C consistently clocks in much faster across different input sizes (N).

For example, let's take N=1. In C, the Iterative method takes a mere 0.000004 seconds, while in Python, it's about 1.192e-06 seconds. Even at N=10, the Dynamic Programming method in C zips through in 0.000001 seconds, while Python lags behind at 1.001e-05 seconds. And as N gets larger, this gap widens. Python's Recursive method starts to drag, taking several seconds for tasks that C handles in fractions of a second.

These differences in execution time can be because of several factors, including:

Language Efficiency: C is a compiled language known for its speed and efficiency, while Python is an interpreted language, which generally results in slower execution.

Memory Management: C allows for more precise memory management, which can lead to faster performance, especially in tasks like Fibonacci calculations where memory usage can be significant.

Algorithm Implementation: Although both languages use similar algorithms for Fibonacci calculations, differences in how the algorithms are implemented in each language can affect performance.

Overhead: Python's dynamic typing and garbage collection introduce overhead that C does not have, which can impact execution time, especially for repetitive tasks like Fibonacci calculations.

In summary, while both Python and C can be used for Fibonacci calculations, C generally offers faster execution times due to its compiled nature, efficient memory management, and lower overhead.

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
In my experience working with both C and Python, I've noticed some interesting differences, especially when it comes to tasks like calculating Fibonacci numbers. C is lightning-fast in executing these calculations, while Python tends to lag behind, especially when the computations get heavier. 

Looking at the data I collected, it's clear that C outshines Python in terms of speed across all methods of calculating Fibonacci numbers. Whether it's using an iterative approach, dynamic programming, or recursion, C consistently finishes the calculations much faster than Python. Even for small values of N, C completes the task in a fraction of the time it takes Python.

Overall, both implementations achieve the same goal of calculating Fibonacci numbers using different approaches. However, there are notable differences in the syntax, memory management, and execution time between C and Python.

In C, I had to manage memory explicitly using arrays for dynamic programming, while in Python, memory management is handled automatically by the interpreter, making the code more concise and readable. However, this convenience in Python comes at a cost of performance, as C executes significantly faster due to its compiled nature and low-level memory access.

During the implementation, I experimented with different optimization techniques, such as memoization in Python and loop unrolling in C, to improve the performance of the recursive approach. However, the gains were modest, and the recursive approach still lagged behind the iterative and dynamic programming approaches in terms of speed.

In conclusion, while Python offers ease of development and readability, C shines in terms of performance and control. The choice between the two languages depends on the specific requirements of the project, balancing factors like speed, development time, and maintainability.

In hindsight, I realize that I should have explored how the code handles larger values of n more thoroughly. While the current implementation works well for small  n values, it may encounter limitations as n grows significantly larger. For example, the recursive approach in Python is limited by the default recursion depth, which may lead to stack overflow errors for very large n values. Increasing the recursion limit using sys.setrecursionlimit() helps to some extent but isn't a scalable solution for extremely large n values. Additionally, considering alternative data structures or libraries specifically designed for handling large numerical computations, such as NumPy for Python, could have provided insights into optimizing performance and memory usage for larger n values.

Overall, a deeper exploration of how the code handles larger n values and potential optimizations for scalability would have enhanced the robustness and applicability of the solutions across a wider range of use cases.

## Conclusions / Reflection

Reflecting on this project, I've gained valuable insights into the differences between C and Python. It's clear that C offers blazing-fast performance, but at the expense of complexity. Python, on the other hand, prioritizes simplicity and readability, albeit with slower execution. Choosing the right language depends on the task at hand. For speed-critical projects like system programming, C is the way to go. Its efficiency and control over hardware make it indispensable. However, for quick development and maintenance, Python shines. Its extensive library and ease of use make it perfect for web development and data analysis. Ultimately, being proficient in both C and Python provides developers with a versatile toolkit. Whether optimizing for speed or readability, having multiple languages at your disposal allows for tailored solutions that meet project needs effectively. Reflecting on my experience, I acknowledge that I faced challenges in figuring out how to effectively handle larger values of n. While I made progress in implementing the Fibonacci algorithms and measuring their performance, I struggled to find optimal solutions for accommodating extremely large n values. This limitation served as a valuable learning experience, highlighting the importance of continuous improvement and problem-solving skills. 

## References
https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/ 

https://en.wikipedia.org/wiki/Fibonacci
