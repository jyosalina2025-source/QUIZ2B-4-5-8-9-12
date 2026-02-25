def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

found = False

for i in range(2, num):
    if is_prime(i) and is_prime(num - i):
        print(f"{num} = {i} + {num - i}")
        found = True
        break

if not found:
    print(f"{num} cannot be expressed as the sum of two prime numbers.")