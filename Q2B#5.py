def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def catalan(n):
    return factorial(2*n) // (factorial(n + 1) * factorial(n))


N = int(input("Enter N (number of terms): "))

print(f"First {N} terms of the Catalan Series:")

for i in range(N):
    print(catalan(i), end=" ")