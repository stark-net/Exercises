from random import choice
def my_random():
    l = []
    for _ in range(10000,99999):
        l.append(_)
    print(choice(l))
my_random()
