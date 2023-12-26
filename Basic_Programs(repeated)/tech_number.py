n = 3025
m = str(n)
a = m[:len(m)//2]
b = m[len(m)//2:]
c = int(a)+int(b)
d = c**2

if(d==n):
    print("Tech number")
else:
    print("Not a Tech number")
