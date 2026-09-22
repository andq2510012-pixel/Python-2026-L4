a = [1,2,3,4,5,6,7,8,9]

def extract_even(n):
    for i in range(0, 8):
        if n[i]%2 == 0:
            new_n = n[i]
            print(new_n, end=" ")
extract_even(a)