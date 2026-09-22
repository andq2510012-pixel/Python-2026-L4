x = (int(input()))
if x < 0:
    print("cannot calculate!")
else:
    def factorial(n):
        factorial = 1
        for i in range (1,n+1):
            factorial *= i
        return factorial
print(factorial(x))
