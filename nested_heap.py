class min_heap:
    def __init__(self,max_size):
        self.max_size=max_size
        self.arr=[None]*max_size
        self.heap_size=0

    def insert(self,ele):
        if self.heap_size==None:
            return 
        self.arr[self.heap_size]=ele
        self.heap_size+=1
        i=self.heap_size-1
        parent = (i-1)//2
        while i>0 and self.arr[parent][0] > self.arr[i][0]:
            self.arr[parent],self.arr[i]=self.arr[i],self.arr[parent]
            i=parent
            parent=(i-1)//2
