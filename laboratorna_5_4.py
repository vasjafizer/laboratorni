import math

n= int(input("Ввідіть значення n :"))
x_3=0
x_2=9
x_1=-9
x_n=0
for i in range(3,n+1) :
    x_n=math.sin(x_3)+2*x_1+3*x_2
    x_2=x_1
    x_1=x_3
    x_3=x_n
print("Значення виразу дорівнює : {0}".format(x_n))
