from typing import Any, Union

b = 0
agelist = []
while b < 10:
    import random, time
    x = random.randint(1,10)
    print('你输入了：%s' % x)
    print('正在计算中，程序将实时展示计算数据')
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
        print('你的生日：过了')
        num = sum
        sum += 1770
        print('%s+1770=%s' % (num, sum))
    elif y == 2:
        print('你的生日：没过')
        num = sum
        sum += 1769
        print('%s+1769=%s' % (num, sum))
    a = random.randint(2020-100,2020)
    print('你的出生年是：%s' % a)
    num = sum
    sum = sum - a
    print('%s+%s=%s' % (num, a, sum))
    num = x
    x = x * 100
    print('%s*100=%s' % (num, x))
    num = sum
    sum = sum - x
    print('%s-%s=%s' % (num, x, sum))
    print('你的年龄是：%s周岁' % sum)
    agelist.append(sum)
    b=b+1
print(agelist)