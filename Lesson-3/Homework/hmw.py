###List questions

listbek=['a','b','c','d','a','a']
a="a"
print(f'count of a is : {listbek.count('a')}')
numers=[23,56,12,40,12344]
print(sum(numers))
print(max(numers))
print(min(numers))
a=12
print(a in numers)
#6
if numers[0]!=None:
    print(numers[0])
else:
    print("List is empty")
# Alternative approach
if not numers[0]:
    print("List is empty")
else:
    print(numers[0])
#7
if numers[-1]:
    print(numers[-1])
else:
    print("List is empty")
#8
numers2=numers[0:2]
print(numers2)
print(numers)

#9
numers.reverse()
numers3=numers
print(numers3)
#10
numers.sort()
numers4=numers
print(numers4)
#11
original=['ala','bala',34,'ala',45, True]
list(set(original))

#12
original=['ala','bala',34,'ala',45, True]
element=56
original.insert(2,element)
print(original)
#13
element2='ala'
print(original.index(element2))
#14
print(not original)
#15
nums=[2,13,24,10,45]
counts=0
for e in nums:
    if e%2==0:
        counts+=1
print(counts)
#16
odd_counts=0
for e in nums:
    if e%2==1:
        odd_counts+=1
print(odd_counts)
#17
list1=['a','c','f']
list2=['d','w','l']
list3=list1+list2
print(list3)
#18
listcha=[[1,2],[3,6],[4,8]]
sublist=[3,6]
print(sublist in listcha)
#19
List=['a','c','d','a','b','c']
old='c'
new='l'
if old in List:
    i=List.index(old)
    List[i]=new
print(List)
#20
raqam=[2,3,4,6,8]
maks=max(raqam)
raqam.remove(maks)
print('2nd largest:',max(raqam))

#21
minm=min(raqam)
raqam.remove(minm)
print(f'2nd smallest : {min(raqam)}')
#22
raqam1=[2,4,5,7,8,24]
raqam2=[]
for e in raqam1:
    if e%2==0:
        raqam2.append(e)
print(raqam2)
#23
raqam3=[]
for e in raqam1:
    if e%2==1:
        raqam3.append(e)
print(raqam3)
#24
raqam2=[2, 4, 8, 24]
print('number of elemnts:',raqam2.__len__())
#25
raqam3=[5,7]
raq=raqam3.copy()
print(raq)
#26
d=['d','dd','ddd','ddd','dddd']
n=len(d)
mid=n//2
if n%2==1:
    print(d[mid])
else:
    print(d[mid-1],d[mid])
#27
big=[[2,3],[3,5],[99,234]]
small=[3,5]
if small in big:
        print(max(small))
#28
big=[[2,3],[3,5],[99,234]]
small=[3,5]
if small in big:
        print(min(small))
#29
l=['rock','paper','scissors']
index_e=1
if len(l)>index_e:
    print(l[index_e])
else:
    print('Index doesn\'t exists')

#30
l1=[2,3,4,45]
print(l1==sorted(l1))
#31
list31=['a','c','o']
numer=2
lis31=[]
for e in list31:
    lis31.append([e]*numer)
print(lis31)
#32
my_list=['fa','od','rh']
your_list=['di','xa','cha']
our_list=sorted(my_list+your_list)
print(our_list)
#33
myList=['sa','la','da',3,'da','34','da']
my_element='da'
indices=[i for i,x in enumerate(myList) if x==my_element]
print(indices)
#34
old_list=[2,4,5,2,6]
k=len(old_list)//2
rotated=old_list[-k:]+old_list[:-k]
print(rotated)

#35
list_num=[]
r=range(1,11)
for n in r:
    list_num.append(n)
print(list_num)
#36
numbers=[-1,2,45,-6,3]
positive=[]
for n in numbers:
    if n>0:
        positive.append(n)
print(sum(positive))
#37
numbers=[-1,2,45,-6,3]
negative=[]
for n in numbers:
    if n<0:
        negative.append(n)
print(sum(negative))
#38
lists=[1,2,1,2]
if lists==lists[::-1]:
    print('palindrome')
else:
    print('not palindrome')
#39
original_list=[1,1,1,2,2,2,3,3]
sub1=[1]
sub2=[1]
sub3=[1]
sub4=[2]
sub5=[2]
sub6=[2]
sub7=[3]
sub8=[3]
nested=[]
nested=[sub1]+[sub2]+[sub3]+[sub4]+[sub5]+[sub6]+[sub7]+[sub8]
print(nested)
#40
given=[52,0,5,2,0,0]
filtered=[]
for e in given:
    if e not in filtered:
        filtered.append(e)

print(filtered)


#Tuple

#1
t=(2,3,2,4,2)
print(t.count(2))
#2
print(max(t))
#3
print(min(t))
#4
print(4 in t)
#5
if t[0]:
    print(t[0])
else:
    print('nothing')
#6
if t[-1]:
    print(t[-1])
else:
    print('nothing')
#7
print(f'Lenth of t is {len(t)}')
#8
t2=t[:3]
print(t2)
#9
tuplee=('a','b')
tupleee=('d','f')
tupleeee=tupleee+tuplee
print(tupleeee)
#10
tt=()
if tt:
    print(tt)
else:
    print('empty')
#11
el=2
indices_el=[]
for i in range(len(t)):
    if t[i]==el:
        indices_el.append(i)
print(indices_el)
#12
tuplebek=(5,56,89,3,4)
sorted_t=sorted(tuplebek)
print(sorted_t[-2])
#13
tuplebek=(5,56,89,3,4)
sorted_t=sorted(tuplebek)
print(sorted_t[1])
#14
elem=1
tuple(elem)
#15
listed=[2,3,56,3,4]
tuple(listed)
#16
tople=(3,4,5,1)
print(tople==tuple(sorted(tople)))
#17
bigT=((2,4),(345,1),(2,345))
smallT=(345,1)
if smallT in bigT:
    print(max(smallT))
#18
bigT=((2,4),(345,1),(2,345))
smallT=(345,1)
if smallT in bigT:
    print(min(smallT))
#19
q=('l','o','v')
q1='o'
qq=list(q)
qq.remove(q1)
new_q=tuple(qq)
print(new_q)
#20
og_t=('w','e','r','t')
listed_t=list(og_t)
new_l=[]
for e in listed_t:
    new_l.append(tuple(e))
new_t=tuple(new_l)
print(new_t)
#21
og_t=('w','e','r','t')
digt=4
list(og_t)
lt=[]
for e in og_t:
    lt.append([e]*digt)
tuple(lt)
print(lt)
#22
range_num=range(3,31)
num_t=[]
for num in range_num:
    num_t.append(num)
tuple(num_t)
print(num_t)
#23
og_t=('w','e','r','t')
ogt=list(og_t)
ogt.reverse()
reverse_t=ogt
print(reverse_t)
#24
og_t=('w','e','r','t')
org=og_t[::-1]
print(org==og_t)
#25
og_t=('w','e','r','t','e')
list(og_t)
newogt=[]
for e in og_t:
    if e not in newogt:
        newogt.append(e)
tuple(newogt)
print(newogt)

###SET
#1
my_set={2,3,4}
my_set2={3,5,9}
my_set3=my_set.union(my_set2)
print(my_set3)
#2
my_set4=my_set.intersection(my_set2)
print(my_set4)
#3
my_set5=my_set.difference(my_set2)
print('Difference:',my_set5)
#4
main={'r','a','h','m','a','t'}
sub={'r','a','t'}
print(sub.issubset(main))
#5
main={'r','a','h','m','a','t'}
elemnt='h'
print(elemnt in main)
#6
mmain={'r','a','h','m','a','t'}
print(f'Length of set: {len(mmain)}')
#7
lis=[2,4,5,7,3,2,5,0,4]
sett=set(lis)
print(sett)
#8
main={'r','a','h','m','o','t'}
rem_el='a'
list(main)
main.remove(rem_el)
set(main)
print(main)
#9
main={'r','a','h','m','a','t'}
main.clear()
newM=main
print(newM)
#10
main={'r','a','h','m','t'}
if main:
    print('not empty')
else:
    print('empty set')
#11
setbek={23,34,45}
setjon={34,16}
setboy=setbek.symmetric_difference(setjon)
print(setboy)
#12
main={'r','a','h','m','a','t'}
add_el='!'
if add_el not in main:
    main.add(add_el)
print(main)
#13
main={'r','a','h','m','a','t'}
removd=main.pop()
print(removd)
#14
num_set={2,345,5674,43567598}
max_el=max(num_set)
print(max_el)
#15
num_set={2,345,5674,43567598}
min_el=min(num_set)
print(min_el)
#16
num_set={2,345,5674,43567598,3}
even_num=set()
for e in num_set:
    if e%2==0:
        even_num.add(e)
print(even_num)

#17
num_set={2,345,5674,43567598,3}
odd_num=set()
for e in num_set:
    if e%2==1:
        odd_num.add(e)
print(odd_num)
#18
range_set=set()
num_range=range(2,7)
for num in num_range:
    range_set.add(num)
print(range_set)
#19
thor={'thunder','mjolnir','asgard'}
hulk={'smash','Banner','angry','thunder'}
avanger=thor.union(hulk)
print(avanger)
#20
thor={'thunder','mjolnir','asgard'}
hulk={'smash','Banner','angry'}
if thor.intersection(hulk):
    print(thor.intersection(hulk))
else:
    print('nothing common')
#21
yu=[2,3,2,3,2,32,33]
yu=set(yu)
yu=list(yu)
print(yu)
#22
you=[2,3,2,3,2,32,33]
you=set(you)
print("Length:",len(you))
#23
import random
n=10
nu=[random.randint(15,35 ) for _ in range(n)]

random_set=set(nu)
print(random_set)
#Dictionary

#1
dictn={'name':'Fred'}
if dict['name']:
    print(dict['name'])
else:
    print('no key')
#2
dikt={'name':'Fred',
      'age':20,
      'sex':'M',
      'nationality':'uzbek'}
test_key='Lname'
print(test_key in dikt.keys())
#3
print('num of keys:',len(dikt.keys()))
#4
keys_dkt=dikt.keys()
print(keys_dkt)
#5
value_dkt=dikt.values()
print(value_dkt)
#6
dic1={'company':'Samsung',
      'model':'A23'}
dic2={'colour':'grey',
       'price':2800000}
phone=dic1 | dic2
print(phone)
#7
dikt7={'name':'Fred',
      'age':20,
      'sex':'M',
      'nationality':'uzbek'}
key_r='sex'
dikt7.pop(key_r)
print(dikt7)
#8
dikt8={'name':'Fred',
      'age':20,
      'sex':'M',
      'nationality':'uzbek'}
dikt8.clear()
new_dikt=dikt8
print(new_dikt)
#9
dikt9={'name':'Fred',
      'age':20,
      'sex':'M',
      'nationality':'uzbek'}
dikt2={}
if dikt2:
    print('not empty')
else:
    print('empty')
#10
dikt10={'name':'Fred',
      'age':20,
      'sex':'M',
      'nationality':'uzbek'}
keyy='age'
if keyy in dikt10.keys():
    print(f'{keyy}:{dikt[keyy]}')
else:
    print('key does not exist')
#11
dikt11={'name':'Fred',
      'age':20,
      'sex':'M',
      'nationality':'uzbek'}
dikt11.update({'age':'19'})
print(dikt11)
#12
dikt12={'name':'Fred',
      'age':20,
      'sex':'M',
      'nationality':'uzbek',
      'parent\'s nationality':'uzbek'}
x=sum(value=='uzbek' for value in dikt12.values())
print('uzbek appeared:',x)
#13
dikt13={'name':'Fred',
      'age':20,
      'sex':'M',
      'nationality':'uzbek'}
diktt={ v:k for k,v in dikt13.items()}
print(diktt)

#14
dikt14={'name':'Fred',
      'age':20,
      'sex':'M',
      'nationality':'uzbek'}
val='Fred'
for k,v in dikt14.items():
    if v==val:
        print(k)
#15
key_list = ['fruit', 'vegetable', 'car']
value_list = ['apple', 'potato', 'BMW']

dict15 = dict(zip(key_list, value_list))
print(dict15)


#16
# dictionary={'person': {'name':'abu',
#                        'age':'23'},
#             'id':1,
#             'order':'laptop'}
# for v in dikt.values():
#     if type(v)==type(dikt):
#         print('nested')
#     else:
#         print('regular')
dictionary={'person': {'name':'abu',
                       'age':'23'},
            'id':1,
            'order':'laptop'}

has_nested = False

for value in dictionary.values():
    if isinstance(value, dict):
        has_nested = True
        break

print(has_nested)

    
#17
dictionary={'person': {'name':'abu',
                       'age':'23'},
            'id':1,
            'order':'laptop'}
for v in dictionary.values():
    if type(v)==type(dikt):
        print(v.values())
#18
from collections import defaultdict


d = defaultdict(int)

d["a"] += 1
d["b"] += 2

print(d)
print(d["c"])   


#19
dictionary={'person': {'name':'abu',
                       'age':'23'},
            'id':1,
            'order':'laptop',
            's': 'laptop'}
listi=[]
for v in dictionary.values():
    if v not in listi:
        listi.append(v)
print(f'number of unique values is {len(listi)}')
#20
dictionary={'person': 'bb',
            'id':1,
            'order':'laptop',
            's': 'laptop'}
t_dik=tuple(dictionary.items())
t_dik=sorted(t_dik)
dicc=dict(t_dik)
print(dicc)
#21
dictionary={'person': 'bb',
            'id':'d',
            'order':'laptop',
            's': 'laptop'}
t_dik=sorted(dictionary.items(), key=lambda x:x[1])

dicc=dict(t_dik)
print(dicc)
#22
dictionary={'person': 'bb',
            'id':'d',
            'order':'laptop',
            's': 'laptop'}
lit={}
for k,v in dictionary.items():
    if len(v)>1:
        lit[k]=v
print(lit)


#23
dictionary={'name': 'bob',
            'id':'d',
            'order':'laptop',
            's': 'laptop'}
dikt23={'name':'Fred',
      'age':20,
      'sex':'M',
      'nationality':'uzbek'}
d1=set(dictionary.keys())
d2=set(dikt23.keys())
if d1.intersection(d2):
    print('Common key is',d1.intersection(d2))
else:
    print('no common key')
#24
tuple_ver=((2,4),(5,6),(7,9))
dic_ver=dict(tuple_ver)
print(dic_ver)
#25
dikt25={'name':'Fred',
      'age':20,
      'sex':'M',
      'nationality':'uzbek'}
y=dikt25.items()
y=list(y)

print(y[0])