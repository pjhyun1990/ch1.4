# while

count = 1

while count < 5:
    print(count)
    count = count + 1

for count in range(1,5):
    print(count)

# 1 ~ 10 까지 더하는

sum = 0

while sum < 55:
    sum +=1

print(sum)


# 1 ~10

s, i = 0 , 1
while i <= 10:

    s += i
    i += 1

print(s)


i = 0
while i < 10:
    i += 1

    if i < 5:
        continue

    print(i, end=' ')

    if i > 10:
        break

else:
    print('else block')

# 무한루프
i = 0
while True:
    print(i, end=" ")
    if i > 5000000000000000000000000:
        break
    i += 1

else:
    print('else block')