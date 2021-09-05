def bestSum(targetSum, numbers):
    
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    shortestCombination = None

    for num in numbers:
        remainder = targetSum-num
        remainderCombination = bestSum(remainder, numbers)
        if remainderCombination != None:
            combination = remainderCombination+[num]
            # if the combination is shorter than the current 'shortest' update it
            if (shortestCombination == None) or (len(combination) < len(shortestCombination)):
                shortestCombination = combination
 
    return shortestCombination
    


result = bestSum(8, [1,4, 5])
print(result)