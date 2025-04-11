class Queue:
    def __init__(self):
        self.__array = []
        self.__front = 0
        self.__count = 0
    def enqueue(self,ele):
        self.__array.append(ele)
        self.__count+=1
    def dequeue(self):
        if self.__count==0:
            return -1
        ele = self.__array[self.__front]
        self.__front = self.__front+1
        self.__count-=1
        return ele
    def front(self):
        if self.__count==0:
            return -1
        ele = self.__array[self.__front]
        return ele
    def is_empty(self):
        return self.__count == 0

    def size(self):
        return self.__count

a = Queue()
a.enqueue(10)
a.enqueue(11)
a.enqueue(12)
a.enqueue(13)
print(a.dequeue())
print(a.dequeue())
print(a._Queue__count)