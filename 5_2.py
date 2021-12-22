f = input('Enter Filename : ')
fn = open(f,'r')
data = fn.read()
num = [int(x) for x in data.split(',')]
num.sort()
print('The 9th Minimum number is {}'.format(num[8]))
fn.close()
