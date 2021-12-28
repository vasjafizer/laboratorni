a = []
m = []
with open("my.txt") as file:
    for line in file:
        num = int(line)
        a.append(num)
    print(a)
    i = 0
    while i < len(a):
        if a[i]>=10 and a[i]//10%2==0:
            del a[i]
        elif a[i]<10 and a[i]%2==0:
            del a[i]
        else:
            i +=1

    print(a)