class queue:
    st=None
    front=-1
    rear=-1
    queue_size=0
    def __init__(self,queue_size):
        self.st=[None]*queue_size
        self.front=-1
        self.rear=-1
        self.queue_size=queue_size
    def enqueue(self, element):
        if self.rear == self.queue_size:
            pass
        elif self.rear == -1 and self.front == -1:
            self.rear=self.front =  0
            self.st[self.rear] = element
        else:
            self.rear += 1
            self.st[self.rear] = element
    def dequeue(self):
        if self.front == self.rear:
            self.front=self.rear = -1
        else:
            element = self.st[self.front]
            self.front += 1

    def display(self):
        for i in range(self.front, self.rear + 1):
            print(self.st[i])

ans = queue(10)
ans.enqueue(10)
ans.enqueue(20)
ans.enqueue(30)
ans.enqueue(40)
ans.display()
ans.dequeue()
print("after dequeue")
ans.display()
