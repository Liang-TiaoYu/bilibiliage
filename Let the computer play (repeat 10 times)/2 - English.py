from typing import Any, Union

b = 0
agelist = []
while b < 10:
    import random, time
    x = random.randint(1,10)
    print('You entered:%s' % x)
    print('In the process of computing, the program will display the calculated data in real time.')
    sum = x * 2
    print('%s*2=%s' % (x, sum))
    num = sum
    sum += 5
    print('%s+5=%s' % (num, sum))
    num = sum
    sum = sum * 50
    print('%s*50=%s' % (num, sum))
    y = random.randint(1, 2)
    if y == 1:
        print("Your birthday: it's over")
        num = sum
        sum += 1770
        print('%s+1770=%s' % (num, sum))
    elif y == 2:
        print('Your birthday: no')
        num = sum
        sum += 1769
        print('%s+1769=%s' % (num, sum))
    a = random.randint(2020-100,2020)
    print('Your year of birth is:%s' % a)
    num = sum
    sum = sum - a
    print('%s+%s=%s' % (num, a, sum))
    num = x
    x = x * 100
    print('%s*100=%s' % (num, x))
    num = sum
    sum = sum - x
    print('%s-%s=%s' % (num, x, sum))
    print('Your age is: %s years old' % sum)
    agelist.append(sum)
    b=b+1
print(agelist)