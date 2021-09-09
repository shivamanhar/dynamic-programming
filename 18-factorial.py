def fact(n):
    print(f"factorial() called with n= {n}")
    if n == 1:
        return 1
    return_value = n*fact(n-1)
    print(f"-> factorial({n}) returns {return_value}")
    return return_value


result = fact(4)
print(result)