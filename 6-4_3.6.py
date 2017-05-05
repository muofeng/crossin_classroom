total = 0


def add(x):
    global total
    total += x


def multi(x):
    global total
    total *= x

add(10)
multi(3)
print(total)
