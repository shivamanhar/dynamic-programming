def sum(myArry):
    if len(myArry) == 0:
        return 0

    rest = myArry[1::]
    return myArry[0]+ sum(rest)

result = sum([1, 5, 7, -2])
print(result)