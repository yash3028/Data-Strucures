class MinHeap:
    def __init__(self, max_size):
        self.arr = [None] * max_size
        self.heap_size = 0
        self.max_size = max_size

    def heapify(self, i):
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < self.heap_size and self.arr[l] < self.arr[smallest]:
            smallest = l
        if r < self.heap_size and self.arr[r] < self.arr[smallest]:
            smallest = r
        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.heapify(smallest)
    
    def insert(self, element):
        if self.heap_size == self.max_size:
            pass
        self.arr[self.heap_size] = element
        self.heap_size += 1
        i = self.heap_size - 1
        parent = (i - 1) // 2
        while i > 0 and self.arr[parent] > self.arr[i]:
            self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
            i = parent
            parent = (i - 1) // 2

    def print_heap(self):
        for i in range(self.heap_size):
            print(self.arr[i], end=" ")
        print()
    
    def extract_min(self):
        root = self.arr[0]
        self.arr[0] = self.arr[self.heap_size - 1]
        self.heap_size -= 1
        self.heapify(0)
        return root

ans=MinHeap(10)
ans.insert(10)
ans.insert(1)
ans.insert(20)
ans.insert(5)
ans.insert(9)
ans.insert(50)
ans.print_heap()
ans.extract_min()
ans.print_heap()