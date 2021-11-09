a=int(input("Введіть кількість цифр в числі х: "))
x=int(input("Ведіть перше число : "))
b=int(input("Введіть кількість цифр в числі y :"))
y=int(input("Ведіть друге число : "))
suma = 0
while x > 0:
    digit = x % 10
    suma = suma + digit

    x=x // 10
    arithmeticmeanx = suma / a
suma = 0
while y > 0:
    digit = y % 10
    suma = suma + digit
    y=y // 10
    arithmeticmeany = suma/b
if  arithmeticmeanx > arithmeticmeany :
    print("найбільше середнє арифметичне числа x")
else :
    print("найбільше середнє арифметичне числа y")



