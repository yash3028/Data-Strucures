class stack:
    def __init__(self,max_size):
        self.st=[None] * max_size
        self.stack_size=0
        self.max_size=max_size
    
    def push(self,element):
        if self.stack_size==self.max_size:
            return
        else:
            self.st[self.stack_size]=element
            self.stack_size+=1
    
    def pop(self):
        if self.stack_size==0:
            return
        else:
            pop=self.st[self.stack_size-1]
            self.stack_size-=1
            return pop
        
    def peep(self):
        return self.st[self.stack_size-1]
    
    def size(self):
        res = self.stack_size
        return res
    
    def print(self):
        n=self.stack_size
        for i in range(n):
            print(self.st[i],end=" ")
        print()

ans=stack(10)
ans.push(40)
ans.push(20)
ans.push(30)
ans.push(50)
ans.print()
