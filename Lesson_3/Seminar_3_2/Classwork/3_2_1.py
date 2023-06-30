s = input("Enter your string: ").split()
print(s)
l = {}
r = ''
for i in range(len(s)):
    if s[i] not in l.keys():
        l[s[i]] = 1
        r+= f'{s[i]} '
    else:
        r += f'{s[i]}_{l[s[i]]} '
        l[s[i]] +=1
print(r)