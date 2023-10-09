line_numbers = 0
first_cat = -1
while True:
    line = input()
    line_numbers += 1

    if  'кот' in line or 'Кот' in line:
        if first_cat == -1:
            first_cat = line_numbers

    if line == 'СТОП':
        break

print(f"{line_numbers - 1} {first_cat}")
