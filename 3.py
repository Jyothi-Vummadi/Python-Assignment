def is_prime(m):
    for i in range(2,m):
        if m%i == 0:
            return False
    return True

n = int(input('Enter number : '))
lst = [2]
count = 1
i = 3
while(count<n+1):
    if is_prime(i):
        lst.append(i)
        count+=1
    i+=1
print(round(lst[-1]**0.5,7))
