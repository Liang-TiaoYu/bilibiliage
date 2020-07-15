import datetime
print("In the process of computing, the program will display the calculated data in real time.")
a = int(input('Please enter the year of birth'))
b = datetime.datetime.now().year
print('Getting this year: this year is%s' % b)
sum = b - a
print('%s-%s=%s' % (b,a,sum))
print('Your age is: %s years old' % sum)
