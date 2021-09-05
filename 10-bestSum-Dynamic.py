def bestSum(targetSum, numbers, memo={}):

    if targetSum in memo.keys():
        return memo[targetSum]
    
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    shortestCombination = None

    for num in numbers:
        remainder = targetSum-num
        remainderCombination = bestSum(remainder, numbers, memo)
        if remainderCombination != None:
            combination = remainderCombination+[num]
            # if the combination is shorter than the current 'shortest' update it
            if (shortestCombination == None) or (len(combination) < len(shortestCombination)):
                shortestCombination = combination
 
    memo[targetSum] = shortestCombination;
    return shortestCombination
    


result = bestSum(100, [1,2, 25,25])
print(result)