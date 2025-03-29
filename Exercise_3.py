n = int(input("Enter number of the columns of matrix: "))
m = [[0] * n for _ in range(n)]
for row in range(n):
    while(True):
        try:
            value = input(f"Enter value of row ({row}): ")
            m[row] = value
            break
        except:
            print("Enter number in correct form(1 or 0)")
else:
    for j in m:
        for i in j:
            print(i, end=' ')
        print()