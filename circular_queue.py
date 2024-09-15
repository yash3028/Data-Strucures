class circular_queue:
    st=None
    front=-1
    rear=-1
    queue_size=0
    def __init__(self, queue_size):
        self.st = [None] * queue_size
        self.front = -1
        self.rear = -1
        self.queue_size = queue_size

    def enqueue(self, element):
        if (self.rear + 1) % self.queue_size == self.front:
            pass
        elif self.front == -1:
            self.front = self.rear = 0
            self.st[self.rear] = element
        else:
            self.rear = (self.rear + 1) % self.queue_size
            self.st[self.rear] = element

    def dequeue(self):
        if self.front == -1:
            pass
        elif self.front == self.rear:
            element = self.st[self.front]
            self.front = self.rear = -1
        else:
            element = self.st[self.front]
            self.front = (self.front + 1) % self.queue_size

    def display(self):
        i = self.front
        while i!=self.rear:
            print(self.st[i], end=' ')
            i = (i + 1) % self.queue_size
        print() 

ans = circular_queue(10)
ans.enqueue(10)
ans.enqueue(20)
ans.enqueue(30)
ans.enqueue(40)
ans.display()
ans.dequeue()
print("after dequeue")
ans.display()
