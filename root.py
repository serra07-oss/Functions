def square_root(i):
    eps=0.001
    inc=0.1
    guess=0
    while abs(guess**2-i)>eps and guess**2 < i:
        guess=guess+inc
    return guess

def square(n,epsilon):
    a=n-epsilon
    b=n+epsilon
    increment=0
    for c in range(n**3):
        if b>=square_root(c)>=a:
            increment=increment+1
    return increment

print(square(10,0.001))

