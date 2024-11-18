"""1"""
from random import randint

print('1:')
"""א"""
list16: list[str] = ["Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]
print('the original', list16)
print('a:')
print(sorted(list16, key=lambda w: len(w)))
print('b:')
print(sorted(list16, key=lambda w: len(w.split())))
print('c:')
print(sorted(list16, key=lambda w: w.endswith(w)))
print('d:')
print(sorted(list16, key=lambda w: w[::-1]))
print('e:')
print(sorted(list16, key=lambda w: 'a' in w.lower()))
print('f:')
f_list: list[str, int] = [["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050, "Europe"], \
                          ["London", 2240, "Europe"], ["Sydney", 8780, "Australia"], \
                          ["Dubai", 1300, "Asia"], ["Shanghai", 4920, "Asia"]]
print('f.a:')
print(sorted(f_list, key=lambda x: x[1]))
print('f.b:')
print(sorted(f_list, key=lambda x: x[1], reverse=True))
print('f.c:')
print(sorted(f_list, key=lambda x: x[2]))
print('f.d:')
print(sorted(f_list, key=lambda x: (x[2], x[1])))
"""ב"""
list_b: list[int] = [randint(1, 100) for _ in range(50)]
print(list_b)
print('B.1:')
print(sorted(list_b))
print('B.2:')
print(sorted(list_b, key=lambda x: sum(list_b) / len(list_b)))
"""2"""
print('2.a:')
text = 'This chocolate cake is rich, moist, and full of delicious chocolate flavor.\
To make the cake, you will need chocolate, flour, sugar, eggs, and butter.\
After baking the chocolate cake, let the cake cool before adding the chocolate frosting.'
words: list[str] = (text.lower().replace(',', '').replace('.', '').split())
print(words)
dict_count: dict[str:int] = dict()
for i in words:
    dict_count[i] = dict_count.get(i, 0) + 1
print(dict_count)
print('The word that was the most times:', max(dict_count, key=dict_count.get))

print('2.b:')
dict_l: dict[str:int] = dict()
for i in text.lower():
    if i in dict_l:
        dict_l[i] += 1
    else:
        dict_l[i] = 1

print(dict_l)
print('The letter that was the least times:', min(dict_l, key=dict_l.get))

dict_3: dict[int, int] = dict()
for i in range(1, 21):
    dict_3[i] = i ** 3
print(dict_3)
x: int = (int(input('enter a number:')))
print(dict_3.get(x, 'not exist'))
