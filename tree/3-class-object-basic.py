class A:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


a1= A(10)
print(a1.data)

if a1 is not None:
    a1.left = A(20)


print(a1.left.data)