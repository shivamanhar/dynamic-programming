import math
def binary_search(sortedList, target):
    '''
    1. Binary search required sorted list no metter list is ascending 
    or descending sorted
    2. First of all find mid value
    '''
    low = 0
    high = len(sortedList)-1
    while low <= high:
        mid_index = (low+high)//2
        if sortedList[mid_index] == target:
            return mid_index
        if sortedList[mid_index]  > target :
            high = mid_index-1
        if sortedList[mid_index] < target:
            low = mid_index+1
    
    return -1


myList = [2, 5, 8, 9, 12, 13, 14, 15, 16, 17]

result = binary_search(myList, 14)
print(result)