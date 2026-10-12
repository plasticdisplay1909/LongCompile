class MaxHeap:
    def __init__(self):
        "Initialized as empty heap"
        self.arr=[]

    "Getting child and parents"
    def left(self,idx): return 2*idx+1
    def right(self,idx): return 2*idx+2
    def parent(self,idx): return (idx-1)//2

    "Swap idx1,idx2"
    def swap(self,idx1,idx2):
        self.arr[idx1],self.arr[idx2]=self.arr[idx2],self.arr[idx1]

    "Maximum element"
    def get_max(self):
        if self.arr:
            return self.arr[0]

        return None

    "Insert a new key"
    def insert(self,key):
        self.arr.append(key)
        n=len(self.arr)-1

        # Fixing min heap property
        while n>0:
            m=self.parent(n)

            if self.arr[m] >=self.arr[n]: break
            else:
                self.swap(n,m)
                n=m

    def extract_max(self):
        if not self.arr: return None

        ans=self.arr[0]
        last=self.arr.pop()

        if self.arr:
            self.arr[0]=last
            self.heapify(0)
        return ans

    def heapify(self,idx):
        n=self.size()

        while True:
            largest=idx
            l,r=self.left(idx),self.right(idx)

            if l<n and self.arr[l]>self.arr[largest]: largest=l
            if r<n and self.arr[r]>self.arr[largest]: largest=r

            if largest==idx: break

            self.swap(idx,largest)
            idx=largest        

    def size(self): return len(self.arr)
    def isempty(self): return len(self.arr)==0
