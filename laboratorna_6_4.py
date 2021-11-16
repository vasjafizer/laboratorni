#Впорядкувати елементи масиву за зростанню модулів елементів
n=int(input("Введіть кількість елементів у масиві : "))
a=[]
for num in range(n) :
    num=int(input("Введіть елемент масиву : "))
    a.append(num)
print(sorted(a, key=abs))

