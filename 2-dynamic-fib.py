'''a = {1:'ravi', 3:'goviend', 4:'hemant'}
if 1 in a.keys():
    print("ok")
    print(a[1])
else:
    print("key not in")
'''

def fib(n,memo={}):
    if n in memo.keys():
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1,memo)+fib(n-2,memo)
    return memo[n]

a = fib(60)

print(a)
