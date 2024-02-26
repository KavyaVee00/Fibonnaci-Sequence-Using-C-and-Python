#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to calculate the nth Fibonacci number iteratively
int iterative_fib(int n) {
    if (n <= 1) {
        return n;
    }
    int a = 0, b = 1, temp;
    for (int i = 2; i <= n; i++) {
        temp = b;
        b += a;
        a = temp;
    }
    return b;
}

// Function to measure the time taken by the iterative function
double iterative_C(int n) {
    clock_t start_time = clock();
    int result = iterative_fib(n);
    clock_t end_time = clock();
    return ((double) (end_time - start_time)) / CLOCKS_PER_SEC;
}

// Function to calculate the nth Fibonacci number using dynamic programming
int fib(int n) {
    int fib[n + 1];
    fib[0] = 0;
    fib[1] = 1;
    for (int i = 2; i <= n; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    return fib[n];
}

// Function to measure the time taken by the dynamic programming function
double dynamic_C(int n) {
    clock_t start_time = clock();
    int result = fib(n);
    clock_t end_time = clock();
    return ((double) (end_time - start_time)) / CLOCKS_PER_SEC;
}

// Recursive function to calculate the nth Fibonacci number
int recursive_fib(int n) {
    if (n <= 1) {
        return n;
    }
    return recursive_fib(n - 1) + recursive_fib(n - 2);
}

// Function to measure the time taken by the recursive function
double recursive_C(int n) {
    clock_t start_time = clock();
    int result = recursive_fib(n);
    clock_t end_time = clock();
    return ((double) (end_time - start_time)) / CLOCKS_PER_SEC;
}

int main() {
    // Open CSV file for writing
    FILE *file = fopen("timing_results.csv", "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Write header row
    fprintf(file, "n,Iterative Timing,Dynamic Timing,Recursive Timing\n");

    // Input value of n
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);

    // Calculate timings for iterative, dynamic, and recursive approaches up to n
    for (int i = 1; i <= n; i++) {
        double iterative_time = iterative_C(i);
        double dynamic_time = dynamic_C(i);
        double recursive_time = recursive_C(i);

        // Write the timings to the CSV file
        fprintf(file, "%d,%lf,%lf,%lf\n", i, iterative_time, dynamic_time, recursive_time);
    }

    fclose(file);
    printf("CSV file 'timing_results.csv' generated successfully!\n");
    return 0;
}
