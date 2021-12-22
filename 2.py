def fib(n):
    ans = []
    a,b = 0,1
    while b<n:
        ans.append(b)
        a,b = b,a+b
    return ans[-1]+ans[-2]

n = int(input("Enter number : "))
print("Fibonacci Number after {0} is ".format(n),end = "")
print(fib(n))
