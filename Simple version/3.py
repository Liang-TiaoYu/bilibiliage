import datetime
print("正在计算中，程序将实时展示计算数据")
a = int(input('请输入出生年'))
b = datetime.datetime.now().year
print('正在获取今年年份：今年是%s' % b)
sum = b - a
print('%s-%s=%s' % (b,a,sum))
print('您的年龄是：%d周岁' % sum)
