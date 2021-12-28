#Обчислити значення виразу
#s=2<a+b, a - b>, де a,b, <x,y> – скалярний добуток векторів..
n=int(input("n = "))
a = [float(input('Введіть координату вектора а {0} :'.format(i))) for i in range(1, n + 1)]
b = [float(input('Введіть координату вектора b {0} :'.format(е))) for е in range(1, n + 1)]
sum=0
for i in range(n):
    res=(a[i]+b[i])*(a[i]-b[i])
    sum+=res
print(sum)