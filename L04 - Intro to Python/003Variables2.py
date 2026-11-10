x = 10
y = x

print(x is y)
print(id(x))
print(id(y))

z = 20

print(x is z)
print(id(z))

x = x + 1

print(x)
print(y)

a = 1000
b = 1000

print(a is b)
