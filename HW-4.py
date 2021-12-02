while True:
    user_word = input('Введите слова: ')
    list = user_word.split()
    for i, word in enumerate(list,1):
        print('{} -  {}'.format(i, word[:10]))