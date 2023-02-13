

######################## Explain Functions of List, Tuple, Set and Dictionary ########################

############# List Functions #################
'''d = ['Raana',123,True,[1],(159,'fgtrd')]
print(d)
print(type(d))'''
'''
lst = ['Rohan','Anil']
lst.append('Purane')
print(lst)
'''
'''
lst = ['Chatrapati','Maharaj']
lst.insert(1,'Shivaji')
print(lst)
'''

'''
lst1 = [1,2,3,4]
lst2 = [19,18,17,16,15]
print(f"List1 : {lst1} and List2 : {lst2}")
print()
lst1.extend(lst2)
print(f"After Extending List2 in List1 : {lst1}")
print()
lst2.extend(lst1)
print(f"After Extending List1 in List2 : {lst2}")
'''
'''
lst1 = [1,2,3,4,5,6]
lst2 = [9,8,6,5,4,]
lst3 = lst1 + lst2
print(lst3)
print(sum(lst3))

summ = 0
for i in(lst1):
    summ += i
print(summ)
'''
'''
lst1 = [1,2,1,3,4,1,1,5,6,1,11,456,178]
print(lst1.count(1))
'''
'''
lst1 = [1,2,1,3,4,1,1,5,6,1,11,456,178,11]
print(lst1.index(11,11))
print(lst1.index(11))
'''
'''
lst1 = [1,2,1,3,4,1,1,5,6,1,11,456,178,11]
print(lst1)
print(lst1.pop())
print(lst1)
print(lst1.pop(0))
print(lst1)
'''
'''
lst1 = [1,2,1,3,4,1,1,5,6,1,11,456,178,11]
print(lst1)
del lst1[1]
print(lst1)
'''
'''
lst1 = [1,2,1,3,4,1,1,5,6,1,11,456,178,11]
print(lst1)
lst1.remove(456)
print(lst1)
'''
'''
lst1 = [1,2,1,3,4,1,1,5,6,1,11,456,178,11]
print(lst1)
lst1.sort()
print('After Sorting : \n',lst1)
'''

############# Tuple Functions #################

# lst2 = ['Chatrapati Shivaji Maharaj']
# print(tuple(lst2))

'''
d = ('Raana',123,True,[1])
print(type(d))
print(d)
'''
'''
d = 'Raana',123,True,[1]
print(type(d))
print(d)
'''
'''
d = ('Raana',123,True,[1,5,9,4,8])
print(d[0][2])
print(d[2])
print(d[3][3])
print(('Repeat,')*3)
'''
'''
a = (3,4,5,68,852,48,3,68,98,5,68,0)
print(max(a))
print(min(a))
'''
'''
a = (3,4,5,68,852,48,3,68,98,5,68,0)
b = ()
print(any(a))
print(any(b))
print(sum(a))
'''
