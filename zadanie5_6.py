sum = 0
count = 0
while True:
    num = int(input())
    sum += num
    count += 1
    if sum == 10:
        print(count)
        break
