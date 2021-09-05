def canSum(targetSum, numbers, memo={}):
    if targetSum in memo.keys():
        return memo[targetSum]

    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    
    for num in numbers:
        remainder = targetSum-num
        if canSum(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True

    memo[targetSum] =False
    return False


#result = canSum(7, [2, 3])
#print(result)
#result = canSum(7, [5,3,4,7])
#print(result)
#result = canSum(7, [2, 4])
#print(result)
#result = canSum(300, [7, 14])
#print(result)


# Time complexty
# O(m*n) time
# O(m) space

