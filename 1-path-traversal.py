from collections import deque

def breathFirstPrint(myGraph, source):
    queue = deque([source])
    while len(queue):
        current  = queue.popleft()
        print(current)
        for neighbor in myGraph[current]:
            queue.append(neighbor)

myGraph = {
    'a':['b', 'c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}

breathFirstPrint(myGraph, 'a')