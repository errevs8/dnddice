import random

list1d4=[1, 2, 3, 4]
list1d6=[1, 2, 3, 4, 5, 6]
list1d8=[1, 2, 3, 4, 5, 6, 7, 8]
list1d10=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1d12=[1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
list1d20=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20]

i1=input("what kind of dice? >")
if i1 == "1d4":
    print(random.choice(list1d4))
if i1 == "1d6":
    print(random.choice(list1d6))
if i1 == "1d8":
    print(random.choice(list1d8))
if i1 == "1d10":
    print(random.choice(list1d10))
if i1 =="1d12":
    print(random.choice(list1d12))
if i1 == "1d20":
    print(random.choice(list1d20))
if i1 == "2d4":
    print(random.choice(list1d4) + random.choice(list1d4))
if i1 == "3d4":
    print(random.choice(list1d4) + random.choice(list1d4) + random.choice(list1d4))
if i1 == "2d6":
    print(random.choice(list1d6) + random.choice(list1d6))
if i1 == "3d6":
    print(random.choice(list1d6) + random.choice(list1d6) + random.choice(list1d6))
if i1 == "2d8":
    print(random.choice(list1d8) + random.choice(list1d8))
if i1 == "3d8":
    print(random.choice(list1d8) + random.choice(list1d8) + random.choice(list1d8))
if i1 == "2d12":
    print(random.choice(list1d12) + random.choice(list1d12))
if i1 == "3d12":
    print(random.choice(list1d12) + random.choice(list1d12) + random.choice(list1d12))
if i1 == "2d20":
    print(random.choice(list1d20) + random.choice(list1d20))
if i1 == "3d20":
    print(random.choice(list1d20) + random.choice(list1d20) + random.choice(list1d20))
