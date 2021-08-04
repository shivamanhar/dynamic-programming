'''def fizzBuzz(n):
    if n == 1:
        print(n)
        return 1
    print(n)
    return fizzBuzz(n-1)
'''

def fizzBuzz(n):
    for i in range(1, n+1):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        if i%3 == 0 and not i%5 == 0:
            print("Fizz")
        if not i%3 == 0 and i%5 ==0:
            print("Buzz")
        if not i%3 == 0 and not i%5 ==0:
            print (i)
if __name__ == '__main__':
    fizzBuzz(10)