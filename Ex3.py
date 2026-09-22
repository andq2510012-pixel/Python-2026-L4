x = int(input())
if x < 1:
    print(x, "is not prime number")
elif x == 2:
    print(x, "is prime number")
else:
    for i in range(2, x):
        if x % i == 0:
            print(x, "is not prime number")
            break
    else:
        print(x, "is prime number")