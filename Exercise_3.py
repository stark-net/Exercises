n = int(input("Enter number of the columns of matrix: "))
m = [[0] * n for _ in range(n)]     #Matrix
for j in range(n):
    print(f"Enter values of row {j}: ")     #To show which row does user assign value to.
    for i in range(n):
        while(True):
            try:
                index_value = int(input(f"\tValue of column[{i}] of matrix in binary: "))
                if index_value in [0, 1]:
                    m[j][i] = index_value
                    break
                else:
                    raise ValueError("The value number, must be 0 or 1 !")
            except:
                print("Enter Number in the correct form (0 or 1)")
else:
    for row in m:
        print(" ".join(map(str, row)))