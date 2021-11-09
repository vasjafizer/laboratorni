import math


# позначення
'''
a - перше число  - float
b - друге число - float
'''
# введення
a = float (input("Ввеіть переше число : "))
b = float (input("Ввеіть друге число число : "))
# знаходження виразів
sum= a + b
product= a * b
average = (a + b) / 2
geometric_mean= math.sqrt(a + b)

print ("сума дорівнює : {0} ""," "добуток дорівнює:  {1} ""," "середнє арифметичне дорівнює : {2} ""," "середнє геометричне дорівнює : {3}" . format (sum,product,average,geometric_mean) )
