m = 4
n = 3
for i in range (1, m+1):
    for j in range(1, n+1):
        if i == 1 or j == 1 or i == m or j == n:
            print('*', end="")
        else: 
            print(" ", end="")
    print()