def depthFirstPrint(myGraph, source ):
    print(source)
    for neighbor in myGraph[source]:
        depthFirstPrint(myGraph, neighbor)




myGraph = {
    'a':['b', 'c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}

depthFirstPrint(myGraph, 'a')