def gridTraveler(m,n):
    if m == 1 and n ==1:
        return 1
    if m == 0 or n == 0:
        return 0
    
    return gridTraveler(m-1, n)+gridTraveler(m,n-1)


result =  gridTraveler(10, 10)
print(result)

# hight of tree n+m
# time complexty O(2^n+m) time
# O(n+m) space