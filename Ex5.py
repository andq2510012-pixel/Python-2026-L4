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