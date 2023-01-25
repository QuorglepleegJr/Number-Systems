a = 0.2
b = 1
out = 0.2
while out == a*b:
    b += 1
    total = 0
    for x in range(b):
        total += a
    out = total
    print(b, out, a*b)
print(b)
#print(2.0 ** 10 + 1)
a = 1
b = 2
n = 0
while a != b:
    n += 1
    a = 2.0 ** n
    b = 2.0 ** n + 1
print(a, b, n)
print(2.0 ** 1024)