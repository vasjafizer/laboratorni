import math

#позначення
'''
a  - сторона АВ 
b  - сторона ВС 
c  - сторона СD 
d  - сторона DA 
x1,y1 - координати  точки А - float
x2,y2 - координати  точки В - float
x3,y3 - координати  точки С - float
x4,y4 - координати  точки D - float
'''
#введення
x1 = float(input("Введіть значення  координати x1 :"))
y1 = float(input("Введіть значення  координати y1 :"))
x2 = float(input("Введіть значення  координати x2 :"))
y2 = float(input("Введіть значення  координати y2 :"))
x3 = float(input("Введіть значення  координати x3 :"))
y3 = float(input("Введіть значення  координати y3 :"))
x4 = float(input("Введіть значення  координати x4 :"))
y4 = float(input("Введіть значення  координати y4 :"))
#знаходження сторін і діагоналей
a = math.sqrt((x2-x1 )**2 + (y2- y1)**2)
b = math.sqrt((x3-x2)**2 + (y3-y2)**2)
c = math.sqrt((x4-x3)**2 + (y4-y3)**2)
d = math.sqrt((x1-x4)**2 + (y1-y4)**2)
d1 = math.sqrt((x3-x1)**2 + (y3-y1)**2)
d2 = math.sqrt((x4-x2)**2 + (y4-y2)**2)
#порівняння властивості
if d1**2 + d2**2 == 2*a*b + c**2 + d**2 :
    print("А,В,С,D - вершини трапеції")
else :
    print("А,В,С,D - не є вершинами трапеції")
