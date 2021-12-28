
def x(i) :
    if i==0:
        return 2
    elif i==1:
        return 3
    elif i==2:
        return 3
    return 7*x(i-1)-x(i-2)*x(i-3)

n=int(input("Введіть значення n :"))
print("x({0}) = {1} ".format(n,x(n)))