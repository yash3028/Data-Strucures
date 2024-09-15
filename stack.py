class stack:
    st=None
    top=-1
    stack_size=0
    def __init__(self,stack_size):
        self.st=[]
        self.top=-1
        self.stack_size=stack_size
    def push(self,element):
        if self.top<self.stack_size-1:
            self.top+=1
            if self.top<len(self.st):
                self.st[self.top]=element
            else:
                self.st.append(element)
    def pop(self):
        if self.top>=0:
            element=self.st[self.top]
            self.top-=1
            return element
    def peep(self):
        return self.st[self.top]

ans=stack()
ans.push(40)
ans.push(20)
ans.push(30)
ans.push(50)
print(ans.peep())
print(ans.size())
ans.pop()
ans.pop()
ans.pop()
for i in range (ans.top+1):
    print(ans.st[i])