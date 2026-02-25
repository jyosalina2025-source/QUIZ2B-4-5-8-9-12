N = int(input("Enter number of terms: "))

total = 0

for i in range(1, N + 1):
    
    if i == 1:
        term = 1
        print("1", end=" ")
    else:
        numerator = i
        denominator = i + 1
        
        if i % 2 == 0:
            term = numerator / denominator
            print(f"+ {numerator}/{denominator}", end=" ")
        else:
            term = - numerator / denominator
            print(f"- {numerator}/{denominator}", end=" ")
    
    total += term

print("\nSum =", total)