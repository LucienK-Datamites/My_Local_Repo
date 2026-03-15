print("Hello World!")

list1=[1,2,2,3,4,5]
list2=[4,4,5,6,7,7]

union1 = list(set(list1) | set(list2))
#intersection = list(set(list1) & set(list2))
inter = [x for x in list1 if x in list2]
union2 = list1+[x for x in list2 if x not in list1]
union3= list1+list2

print(union2)
print(union3)
#print(intersection)
print(inter)
