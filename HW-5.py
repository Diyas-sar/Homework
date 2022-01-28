list = [9,8,7,7,7,6,5,3,3,3,2,1]
num = int(input('Введите число :'))
i = 0
for n in list:
    if num <= n:
        i +=1
    elif num > n:
        break
list.insert(i, float(num))
print(list)
