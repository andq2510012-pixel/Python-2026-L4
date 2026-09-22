x = int(input("Check number: "))
def checkperfect(n):
    if n < 1:
        print(n, "is not perfect number")
    sum = 0 
    for i in range (1, n):
        if n%i == 0:
            sum += i
    if n == sum:
        print(n, "is perfect number")
    else: 
        print(n, "is not perfect number")

checkperfect(x)