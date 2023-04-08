list1=[10,20,'co',7.9,800,98,67,494]
print('original list :',list1)

del list1[2]
print("after deleting element :",list1)

list1.pop(2)
print('after poping :',list1)

list1.pop()
print(list1)

list1.remove(98)
print('after removing :',list1)
