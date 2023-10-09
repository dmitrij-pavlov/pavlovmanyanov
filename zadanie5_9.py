num_lines = int(input())
cat_found = False
lost_dog = False

for _ in range(num_lines):
    line = input()
    if 'кот' in line.lower() or 'Кот' in line:
        cat_found = True
    if 'пёс' in line.lower() or 'Пёс' in line:
        lost_dog = True
        if cat_found:
            break

if cat_found and not lost_dog:
    print("МЯУ")
else:
    print("НЕТ")
