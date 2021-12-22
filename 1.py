def gcd_iterative(a,b):
    gcd = 1
    for i in range(1,a+1):
        if(a%i==0 and b%i==0):
            gcd = i
    return gcd

def gcd_recursive(a,b):
    if(b==0):
        return a
    else:
        return gcd_recursive(b,a%b)

ch = input("Enter 'I' to obtain GCD through Iteration or 'R' to obtain GCD through Recursion : ")
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
if ch.upper() == 'I':
    print('GCD of {0} & {1} is '.format(a,b),end = "")
    print(gcd_iterative(min(a,b),max(a,b)))
elif ch.upper() == 'R':
    print('GCD of {0} & {1} is '.format(a,b),end = "")
    print(gcd_recursive(a,b))
else:
    print('Enter Valid Choice!')
