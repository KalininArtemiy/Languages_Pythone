a = [int(a) for a in input().split]
k = int(input())
i = 0 
while i < k:
    poped = a.pop()
    a.insert(0, poped)
    i += 1
print (a)