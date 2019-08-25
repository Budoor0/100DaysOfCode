import random
x = 1 # int
y = 2.8 # float
z = 1j #complex
l = "-------------"
print(type(x))
print(type(y))
print(type(z))
print(l)

c = -3
print(type(c))
print(l)

v = 34e2
print(type(v))
print(l)

b= 3+4j
n = 4j
print(type(b))
print(type(n))
print(l)
a = float(x) # convert form int to float
d = int(y) # convert form float to int
f = complex(x) # convert from int to complex

print(a)
print(d)
print(f)
#e = int(f) you can't convert complex to anther type
print(l)

print(random.randrange(1,10))
