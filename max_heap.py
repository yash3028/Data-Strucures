from typing import List
class Heap:
    arr=None
    heap_size=0
    max_size=0
    def __init__(self, max_size):
        self.arr = [None]*max_size
        self.heap_size = 0
        self.max_size=max_size

    def heapify(self,i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < self.heap_size and self.arr[l] > self.arr[largest]:
            largest = l
        if r < self.heap_size and self.arr[r] > self.arr[largest]:
            largest = r
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(largest)
    
    def insert(self, element):
        if self.heap_size == self.max_size:
            pass
        else:
            self.arr[self.heap_size] = element
        self.heap_size += 1
        i = self.heap_size - 1
        parent = (i-1)// 2
        while i > 0 and self.arr[parent] < self.arr[i]:
            self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
            i = parent
            parent=(i-1)//2
    def print_heap(self):
        for i in range(self.heap_size):
            print(self.arr[i], end=" ")
        print()
    def extract_max(self):
        temp=self.arr[0]
        self.arr[0]=self.arr[self.heap_size-1]
        self.heap_size-=1
        self.heapify(0)
        return temp

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=Heap(n)
        for i in range(n):
            ans.insert(nums[i])
        for j in range(k-1):
            ans.extract_max()
        return ans.arr[0]
res=Solution().findKthLargest([3,2,3,1,2,4,5,5,6],4)
print(res)
