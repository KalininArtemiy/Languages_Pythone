n = int(input("Enter length: "))
m = int(input("Enter width: "))
k = int(input("Enter size of slice: "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print("Yes")
else: 
    print("NO")