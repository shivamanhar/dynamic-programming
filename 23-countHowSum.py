def countHowSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum <  0:
        return None

    remainderCombination = []

    for num in numbers:
        remainder = targetSum-num
        remainderResult= countHowSum(remainder, numbers)
        if remainderResult != None:
            remainderCombination=  remainderResult+[num]
            return remainderCombination

    return None


result  = countHowSum(7, [1,3, 4])
print(result)