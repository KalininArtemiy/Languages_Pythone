a = [6, 5, 4, 3, 2, 5]
count = 0
i = 1
while i < len(a):
    if a[i] > a[i-1]:
        count += 1
    i += 1
print(count)