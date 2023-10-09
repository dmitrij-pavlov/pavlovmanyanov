login=input('введите логин: ')
if '@' in login:
    print('неккоретный логин')
else:
    print('ОК')
address=input('введите электронный адрес: ')
if not '@' in address:
    print('неккоретный адрес')
else:
    print('ОК')
