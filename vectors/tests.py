from django.test import TestCase

'''
pronto
a = [0, 2, 5, 7, 0 , 5, 9]
b = []

for i in a:
    if i != 0:
        b.append(i)
for i in a:
    if i == 0:
        b.insert(len(b), i)
print(b)
'''

a = [0, 2, 5, 7, 0, 5, 9]
b = []

for i in a:
    if i != 0:
        a = a.append(i)
for i in a:
    if i == 0:
        a = a.insert(len(a), i)

print(a)
