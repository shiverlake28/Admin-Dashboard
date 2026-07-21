import functools
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
    
print(bool("hello"))
print(bool(-10))

for a in enumerate("hello"):
    print(a)
'''
'''
def functions(name,age = 14):
    return name,age

entry = functions("Alice")
print(entry)
def bio(name,age):
    return f"Hello my name is {name} and I am {age} years old"

name = input("Enter your name: ")   
age = input("Enter your age: ")
bio = bio(name,age)
print(bio)
'''
'''
a = "helloo"
if (n := len(a))>5:
    print(f'taking too long {n}' )

def stunames(name,*args, defaultname = "Unknown", **students):
    for keys,student in students.items():
        print(keys,student)

stunames(name = "Alice", age = 25)
'''
'''
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def run(self):
        print(f"runing {self.name}")
player1 = PlayerCharacter("Alice", 25)
player1.run()


class big:
    pass

player = PlayerCharacter("Bob", 30)
ob = big()
print(type(ob))
help(player)

istrue = isinstance(player, PlayerCharacter)
print(istrue)

class small():
    
    def __init__(self,speciality):
        self.speciality = speciality
        print(speciality)
class things(small):

    def __init__(self, speciality, name):
        super().__init__(speciality)
        self.name = name
        print(name)
special = things("Python", "Alice")
print(dir(special))
'''
def multi(x):
    return x*x

print(list(map(multi, [1,2,3,4,5])))

def condi(items):
    return items % 2 == 0

print(list(filter(condi, [1,2,3,4,5])))

my_list = [1,2,3,4,5]
my2list = [6,7,8,9,10]
print(list(zip(my_list, my2list)))

def add(x,y):
    return x+y

print(functools.reduce(add, [1,2,3,4,5]))

























