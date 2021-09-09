def bestSum(targetSum, numbers):
    
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    shortestCombination =  0

    for num in numbers:
        remainder = targetSum-num
        remainderCombination = bestSum(remainder, numbers)
        if remainderCombination != None:
            combination = remainderCombination+[num]
            shortestCombination += 0
            # if the combination is shorter than the current 'shortest' update it
            #if (shortestCombination == None) or (len(combination) < len(shortestCombination)):                
            #    shortestCombination = combination
            

    return shortestCombination
    


result = bestSum(7, [7, 3])
print(result)