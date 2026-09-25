#Ex1
radius = int(input("Enter radius: "))
S = 3.14*radius**2
print(S)
#Ex2
c = int(input("Enter temperature: "))
f = (c*9.5)+32
print(f, "F degree")
#Ex3
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
#Ex4
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
#Ex5
checkperfect(x)

list = ["red", "blue", "green", "black", "white" ]
color = (str(input("Your color: ")))

def check_color(n):
    y = 0
    for i in range (0,5):
        if n == list[i]:
            print("Your color is in index", i, "in my list")
            y = 1
    if y == 0:
        print("Your color is not in my list")
check_color(color)
#Ex6
for i in range (0, 7, 1):
    print(i, end="")

for n in range (1, 11, 3):
    print( n, end="")

for x in range (5,0, -1):
    print( x, end="")

for y in range (6, -3, -2):
    print( y, end="")
#Ex7
s = str(input("Your money: "))

def remove_dollar_sign(n):
    new = n.replace("$", "")
    print(new)

remove_dollar_sign(s)
#Ex8
a = [1,2,3,4,5,6,7,8,9]

def extract_even(n):
    for i in range(0, 8):
        if n[i]%2 == 0:
            new_n = n[i]
            print(new_n, end=" ")
extract_even(a)
#Ex9
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
#Ex10
x = (int(input()))
def divisors(n):
    divisors = []
    for i in range (1, n+1):
        if n%i == 0:
            divisors.append(i)
    return divisors

print(divisors(x))
#Ex11
import math
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1, y1 = 1, 2
x2, y2 = 3, 4

distance = calculate_distance(x1, y1, x2, y2)
print(f"The distance is: {distance:.2f}")
#Ex12
m = 4
n = 3
for i in range (1, m+1):
    for j in range(1, n+1):
        if i == 1 or j == 1 or i == m or j == n:
            print('*', end="")
        else: 
            print(" ", end="")
    print()

