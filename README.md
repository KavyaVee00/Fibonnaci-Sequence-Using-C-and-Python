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

For this analysis, I've opted for Java as my second language. I made this choice because it really just boils down to its widespread usage and strong features, particularly its object-oriented programming (OOP) approach. Java's OOP principles provide a structured way to tackle complex problems like the Fibonacci sequence. I also wanted to challenge myself by using a language that I'm learning along with C :). 

## Empirical Data & Discussion 
For the empirical analysis, I ran each implementation with various input values of n and recorded the execution times. I also compared the number of operations performed by each algorithm for different values of n.

## Language Analysis


### Language 1: C



### Language 2: UPDATE



### Comparison and Discussion Between Experiences


## Conclusions / Reflection

## References
