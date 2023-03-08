a={12,23,56,40}
b={30,23,8,10}
print(a)
print(b)
r=a.intersection(b)
print('intersection :',r)
r=a.union(b)
print('union :',r)
r=a.difference(b)
print('differance :',r)
r=a.symmetric_difference(b)
print('symmetric differance :',r)
a.clear(b)
print(a)
print(b)

