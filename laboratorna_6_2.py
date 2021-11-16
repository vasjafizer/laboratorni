n=int(input("n ="))
b=float(input("Введіть значення b :"))
a_i_2=b
a_i_1=b
A=[b]
for i in range(3,n+1):
    a_i=a_i_2+a_i_1/2**a_i_1
    a_i_2=a_i_1
    a_i_1=a_i
    A.append(a_i)
sum=0
i=1
while i<len(A) :
    sum=sum+A[i]
    i=i+2
print("сума елементів масиву А з непарними індексами дорівнює :{0}".format(sum))


