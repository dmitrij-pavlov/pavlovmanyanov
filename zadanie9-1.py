n = int(input("Введите количество покупок: "))
покупки = []
for i in range(n):
    покупка = input("Введите покупку {}: ".format(i + 1))
    покупки.append(покупка)
print("Список покупок:")
for покупка in покупки:
    print(покупка)
