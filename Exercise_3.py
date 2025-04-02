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

for j in m:
    for i in j:
        Integer_value_of_i = int(i)
        if Integer_value_of_i in [1,0]:
            pass
        else:
            print("Your entered number is not binary")

for j in m:
    for i in j:
        Integer_value_of_i = int(i)
        if Integer_value_of_i == 1:
            c++





else:
    for j in m:
        for i in j:
            print(i, end=' ')
        print()