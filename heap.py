class MaxHeap(object):
    def __init__(self, capacity):
	self.capacity = capacity
        self.harr = [-1 for i in range(self.capacity)]
	self.heapsize = 0
    def left(self, i):
        return 2*i + 1
    def right(self, i):
        return 2*i + 2
    def parent(self, i):
        return (i-1)/2
    def heapify(self, i):
        max_ind = i
	left = self.left(i)
	right = self.right(i)
	if left <= self.heapsize and self.harr[max_ind] < self.harr[left]:
	    max_ind = left
	if right <= self.heapsize and self.harr[max_ind] < self.harr[right]:
	    max_ind = right
	# Swap
	if max_ind != i:
	    self.harr[i], self.harr[max_ind] = self.harr[max_ind], self.harr[i]
	    self.heapify(max_ind)
    def insert(self, data):
        if self.heapsize == self.capacity:
	    raise Exception('Heap Overflow')
	print 'Inserting %s' % data
        self.heapsize += 1
	self.harr[self.heapsize-1] = int(data)
	# Swap
	self.harr[0], self.harr[self.heapsize-1] = self.harr[self.heapsize-1], self.harr[0]
	self.heapify(0)
    def remove(self):
        if self.heapsize == 0:
	    raise Exception('Heap Underflow')
        temp = self.harr[0]
	self.harr[0] = self.harr[self.heapsize-1]
	self.harr[self.heapsize-1] = -1
        self.heapsize -= 1
	self.heapify(0)
	print 'Removing %s' % temp
	return temp
    # Overload to print object
    def __str__(self):
        res = 'Capacity: %s\n' % self.capacity
	res += 'Heap Size: %s\n' % self.heapsize
	res += str(self.harr)
	return res

if __name__ == '__main__':
    heap = MaxHeap(5)
    print heap
    heap.insert(2)
    heap.insert(5)
    heap.insert(3)
    print heap
    heap.remove()
    print heap
    heap.insert(7)
    heap.insert(8)
    print heap
    heap.insert(8)
    print heap
    #heap.insert(3)
    #heap.insert(4)
    #print heap
    [heap.remove() for i in range(7)]
    print heap
