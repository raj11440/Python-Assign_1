def Sum(A, B, C):
    return A + B + C

def Average(A, B, C):
    return (A + B + C) / 3

A = int(input("Enter Marks 1: "))
B = int(input("Enter Marks 2: "))
C = int(input("Enter Marks 3: "))

print("Total Marks =", Sum(A, B, C))
print("Average =", round(Average(A, B, C), 2))