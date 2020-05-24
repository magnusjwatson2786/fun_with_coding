a = 0
y = 0


def evnchk(a):
    global y
    y = int(y)
    if (y % 2) == 0:
        y = (a // 2)
        return int(y)
    else:
        y = (3 * a) + 1
        return int(y)


print('enter number')
y = input()
a = int(y)
while (y != 1):
    print(evnchk(int(y)))
print('<<<<<<<<<<<<I have done it>>>>>>>>>>>>>>>>')
z = input()
