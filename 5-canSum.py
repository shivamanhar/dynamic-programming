def canSum(targetSum, numbers):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    
    for num in numbers:
        remainder = targetSum-num
        if canSum(remainder, numbers) == True:
            return True

    return False


#result = canSum(7, [2, 3])
#print(result)
#result = canSum(7, [5,3,4,7])
#print(result)
result = canSum(7, [2, 4])
print(result)

# O(n^m) time
# O(m) space