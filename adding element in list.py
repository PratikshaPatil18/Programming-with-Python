list1=[10,20,'co',7.9,'ty',800]
print('original list :',list1)

list1.append(222)
print("after append element :",list1)

list1.insert(2,'pratiksha')
print('after insert :',list1)

list2=[20,30,'engineer',3.9]
list1.extend(list2)
print('after extending :',list1)
print('list2 :',list2)
