def even_odd(i):
    return i%2==0


for i in range(1,11):
    if even_odd(i)==True:
        print("Even")
    else:
        print("Odd")