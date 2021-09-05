def howSum(targetSum, numbers):
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum -num
        remainderResult = howSum(remainder, numbers)
        if remainderResult != None:
            return remainderResult+[num]
        

    return None


#result = howSum(7, [2, 3])
#print(result)

result = howSum(7, [2,4])
print(result)