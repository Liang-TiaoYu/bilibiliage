import datetime
x = int(input('请输入1-10的数（大于10或小于1会导致计算错误）'))
if x>10 or x<1:
    print('都告诉你了还能输错')
    exit()
print("正在计算中，程序将实时展示计算数据")
sum = x * 2
print('%s*2=%s' % (x, sum))
num = sum
sum += 5
print('%s+5=%s' % (num, sum))
num = sum
sum = sum * 50
print('%s*50=%s' % (num, sum))
y = input('你的生日过了吗？（输入过了或者没过）')
if y == '过了':
    num = sum
    sum += 1770
    print('%s+1770=%s' % (num, sum))
elif y == '没过':
    num = sum
    sum += 1769
    print('%s+1769=%s' % (num, sum))
else:
    print('都告诉你了还能输错')
    exit()
a = int(input('你的出生年是：（四位数）'))
if a<1000:
    print('都告诉你了还能输错')
    exit()
elif a>datetime.datetime.now().year:
    print('所以你来自未来？')
    exit()
num = sum
sum = sum - a
print('%s-%s=%s' % (num, a, sum))
num = x
x = x * 100
print('%s*100=%s' % (num, x))
num = sum
sum = sum - x
print('%s-%s=%s' % (num, x, sum))
print('你的年龄是：%s周岁' % sum)
