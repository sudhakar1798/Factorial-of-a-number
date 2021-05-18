x=int(input("enter number"))
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
out = factorial(x)
print("factorial of",x,"is",out)