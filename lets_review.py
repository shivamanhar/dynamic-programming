n = int(input())
s = list()
for i in range(0,n):
    myStr = input()
    s.append(myStr)
    
for i in range(0, n):
    oddstr =''
    evnstr =''
    k = 0
    for j in list(s[i]):
        if k%2 !=0:
            oddstr = oddstr+j
        else:
            evnstr = evnstr+j
        k += 1
            
    print(f'{evnstr} {oddstr}')
