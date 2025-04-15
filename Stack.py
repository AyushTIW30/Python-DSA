class Stack:
    def __init__(self):
        self.__array = []
    def push(self,ele):
        self.__array.append(ele)
    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return
        return self.__array.pop()
    def top(self):
        if self.isempty():
            print("there is no element")
            return
        return self.__array[-1]
    def size(self):
        return len(self.__array)

    def isempty(self):
        return self.size()==0

a = Stack()
a.push(10)
a.push(20)
print(a.pop())
print(a.pop())
print(a.pop())