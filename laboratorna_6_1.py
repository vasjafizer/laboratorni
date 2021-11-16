n=int(input("n = "))
x=[]
for i in range(n):
    num=float(input("num  {0} :".format(i)))
    x.append(num)
x=x[::-1]
print(x)





