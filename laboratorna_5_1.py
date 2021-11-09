#позначення
'''
a - чисельник - int
b - знаменник - int
c - підкосинус = float

'''
import math

a = 1
b = 2
c = 0.1
sum =(a/b + math.cos(c))
while a<=9 :
    sum = sum*(a/b + math.cos(c))
    a = a+1
    b = b+1
    c = c+0.1
print("sum = {0}".format(sum))
