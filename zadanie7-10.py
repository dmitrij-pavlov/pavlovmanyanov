shift = int(input('введите шаг шифра:'))
message = input('введи сообщение:')
encrypted_message = ""
alfavit = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯаБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
for letter in message:
    if letter in alfavit:
        index = alfavit.index(letter)
        new_index = (index + shift) % len(alfavit)
        encrypted_message += alfavit[new_index]
    else:
        encrypted_message += letter
print(encrypted_message)
