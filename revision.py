'''
basket = [1,2,3,4,2]
print(basket.index(4))
print(basket.count(2))
basket.pop(0)
print(basket)
basket.remove(2)
print(basket)
list0 =  [1,2,3,4,5]
print(list(range(1, 10)))
a,b,c, * other = [1,2,3,4,5,6,4,7]
print(other)
dict1 = {'keys': 22,'keys0': 228,'keys1': 220,'keys2': 242,'keys3': 12,'lists': [1,2,3,4,5]}
print(dict1.keys())
print(dict1.values())
print(dict1['lists'][2])
print(dict1.get('keys'))
dicts = dict(name = '22')
print(dicts)
print( '22' in dicts.values())
print(dict1.pop('keys'))
dict1.update({'keys3': 22})
print(dict1)
if 22 not in dict1.values():
    print('yes')
    

else:
    friend = True
    msge = 'hello' if friend else 'goodbye' 
    print(msge)
for keys, values in dict1.items():
    print(f'key: {keys} value: {values}')
    '''
print(bool("hello"))
print(bool(-10))

for a in enumerate("hello"):
    print(a)









