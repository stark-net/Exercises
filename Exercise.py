n = int(input("Enter number of the columns of matrix: "))
m = [[0] * n for _ in range(n)]     #Matrix
for j in range(n):
    print(f"Enter values of row {j}: ")     #To show which row does user assign value to.
    for i in range(n):
        m[j][i] = int(input(f"Enter value of column[{i}] of matrix in binary: "))
else:
    for j in range(n):
        for i in range(n):
            print(m[j][i], end=' ')
        print()