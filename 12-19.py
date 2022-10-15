print("12")
print("before")
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)
print("after")
lst=[num**2 if num%2==1 else num ** 4 for num in range (10)]
print(lst)

print()
print("13")
print("before")
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)
print()
print("after")
list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)


print(list_comprehension)

print()
print("14")
print("before")
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)
print("after")
d1={num: num**2 for num in range (1,11) if num%2==1}
print(d1)

print()
print("15")
print("before")
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)
print("after")
d1={num: num**2 if num%2==1 else num//0.5 for num in range (1,11)}
print(d1)

print()
print("16")
print("before")
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension)
print("after")
d1={}
for x in range(10):
    if x**3%4==0:
        d1[x]=x**3
print(d1)

print()
print("17")
print("before")
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)
print("after")
d1={}
for x in range(10):
    if x**3%4==0:
        d1[x]=x**3
    else:
        d1[x]=x
print(d1)

print()
print("18")
print("before")
def foo(x, y):
    if x < y:
        return x
    else:
        return y
print(foo(1,2))
print("after")
foo1=lambda x,y:x if (x<y) else y
print(foo1(1,2))

print()
print("19")
print("before")
foo = lambda x, y, z: z if y < x and x > z else y
print(foo(1,2,3))
print("after")
def foo1 (x,y,z):
    if y<x and x>z:
        return z
    else:
        return y
print (foo1(1,2,3))