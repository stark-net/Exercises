def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
n = int(input("Enter number of the columns of matrix: "))                                                                                                                                                                                     
m = [[0] * n for _ in range(n)]   
sum_of_row = []    
m_int = []                                                                                                                                                                                                        

for row in range(n):                                                                                                                                                                                                                          
    while(True):                                                                                                                                                                                                                              
        try:                                                                                                                                                                                                                                  
            value = input(f"Enter value of row {row} (only 1 and 0, without spaces): ")                                                                                                                                                       
            if any(i not in "01" for i in value) or len(value) != n:                                                                                                                                                                          
                raise ValueError("\tYour entered number is not valid. Please make sure about it.")                                                                                                                                              
            m[row] = [int(i) for i in value]                                                                                                                                                                                                  
            break                                                                                                                                                                                                                             
        except ValueError as error:                                                                                                                                                                                                           
            print(error)                                                                                                                                                                                                                      
    if value == 0:                                                                                                                                                                                                                           
        break

'''for i in range(len(m)):
    sum_of_index = 0
    for j in range(len(m[i])):
        sum_of_index += int(m[i][j])
    sum_of_row.append([sum_of_index])'''
    
    
sum_of_row = [sum(row) for row in m]

print("OK" if all(map(is_even, sum_of_row)) else "Corrupt")



'''print("\nThe matrix is:\n")                                                                                                                                                                                                                                    
for j in m:                                                                                                                                                                                                                               
    for i in j:                                                                                                                                                                                                                           
        print(i, end=' ')                                                                                                                                                                                                                 
    print()'''