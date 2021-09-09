def foo(n):
    print(n)
    if n <= 1:
        return 1
    foo(n-1)

foo(5)

# O(n) time
# O(n) Space

def bar(n):
    print(n)
    if n <=1:
        return 1
    foo(n-2)

bar(5)

# O(n/2) time complexty but we simplyfy this O(n/2) to only 
# O(n) time
# O(n) Space
 
def dib(n):
    if n<=1:
        return 1
    dib(n-1)
    dib(n-2)

# O(2^n) time 
# O(n) space

def lib(n):
    if n<=1:
        return 1
    lib(n-2)
    lib(n-2)

# O(2^n/2) time complexty simplify O(2^n)
# O(n) space


