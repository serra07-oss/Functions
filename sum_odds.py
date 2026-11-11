def even_odd(i):
    return i%2==0

def sum_odds(a,b):
    sum=0
    for i in range(a,b+1):
        if even_odd(i)==True:
            sum=sum
        else:
            sum=sum+i
    return sum

print(sum_odds(1,10))
