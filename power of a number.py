x=int(input("Enter the base value"))
n=int(input("Enter the power value"))
def power(x,n):
    if n==0:
      return 1
    return x* power(x,n-1)
print("The power of base",x,"is",power(x,n))