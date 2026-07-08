def Check(A, B):
    return (A % 10 == 0) or (B % 10 == 0)

A = int(input("Enter A: "))
B = int(input("Enter B: "))

print(Check(A, B))