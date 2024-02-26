#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include <stdint.h>

#define MAX 1000

typedef uint64_t ull;

// Function to calculate the nth Fibonacci number iteratively
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

ull fibonacci_recursive(int n, ull *ops)
{
    if (n <= 1) {
        return n;
    }

    *ops += 1; // Counting one operation for the addition
    return fibonacci_recursive(n - 1, ops) + fibonacci_recursive(n - 2, ops);
}



// Function to calculate the nth Fibonacci number using dynamic programming
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

// Function to time the execution of a Fibonacci function
double time_function(ull (*func)(int, ull *), int n, ull *ops)
{
    struct timespec begin, end;
    clock_gettime(CLOCK_MONOTONIC, &begin);
    ull result = func(n, ops);
    clock_gettime(CLOCK_MONOTONIC, &end);
    return (end.tv_nsec - begin.tv_nsec) / 1000000000.0 + (end.tv_sec - begin.tv_sec);
}

// Function to display program usage
void help()
{
    printf("Usage: ./fibonacci.out N [Type]\n");
    printf("\tN is the index of the Fibonacci number to calculate (required).\n");
    printf("\t[Type] is 1 for iterative, 2 for recursive, and 3 for dynamic programming. Defaults to dynamic programming.\n");
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Error: At least one argument needed!\n");
        help();
        return 1;
    }

    int n = atoi(argv[1]);
    if (n < 0 || n >= MAX)
    {
        printf("Error: Invalid value for N!\n");
        return 1;
    }

    int type = 3;
    if (argc > 2)
    {
        type = atoi(argv[2]);
        if (type < 1 || type > 3)
        {
            printf("Error: Invalid value for Type!\n");
            help();
            return 1;
        }
    }

    for (int i = 1; i <= n; i++)
    {
        ull ops = 0;
        double time;
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

    return 0;
}
