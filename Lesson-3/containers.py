# a=[1,2,3]
# b=a
# a.append(4)
# print(a)
# print(b)
# print(id(a) == id(b))



# a=[3,4,5]
# b=a.copy()
# print(id(a))
# print(id(b))
 

x=[
    [1,2]
    ,[3,4]
]
# y=x.copy()
# x[0].append(5)
# print(x)
# print(y)

from copy import deepcopy
y=deepcopy(x)
x[0].append(6)
print(x)
print(y)