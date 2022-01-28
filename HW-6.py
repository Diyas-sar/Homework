goods =[]
features = {'name': '', 'price': '', 'quantity': '', 'measuerement':''}
analytics = {'name': [], 'price': [], 'quantity': [], 'measuerement':[]}
num = 0
while True:
    if input('Для выхода из приложения нажмите Q, для продолжения Enter: ').upper() == "Q":
        break
    num +=1
    for f in features.keys():
        prop = input(f'Введите свойства {f} - ')
        features[f] = int(prop) if f in ('price', 'quantity') else prop
        analytics[f].append(features[f])
    goods.append((num, features.copy()))
    print(f'\nСтруктура товаров \n{goods}')
    print(f'\nТекущая аналитика по товарам \n{"*" *30}')
    for key, value in analytics.items():
        print(f'{key[:25]:>30}:{value}')
    print("*"*30)
