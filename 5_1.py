f = input('Enter Filename : ')
fn = open(f,'r')
data = fn.read()
num = [int(x) for x in data.split(',')]
num.sort()
print('The 3rd Maximum number is {}'.format(num[-3]))
fn.close()
