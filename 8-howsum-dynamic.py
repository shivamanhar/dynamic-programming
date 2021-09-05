def howSum(targetSum, numbers, memo={}):
    if targetSum in memo.keys():
        return memo[targetSum]

    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum -num
        remainderResult = howSum(remainder, numbers, memo)
        if remainderResult != None:
            memo[targetSum] = remainderResult+[num]
            return memo[targetSum]
        

    memo[targetSum] = None
    return None


#result = howSum(7, [2, 3])
#print(result)

result = howSum(300, [3,2,5,14])
print(result)

# time O(n^m*m)
#O(m) Space
# memorized
# time : O(n*m^2)
# O(m^2) Space
