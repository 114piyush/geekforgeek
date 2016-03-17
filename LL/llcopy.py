import copy

class Node:
    def __init__(self, data):
        self.data = data
	self.next = None
	self.random = None

def PrintList(head):
    while head:
        print '{id: %s, data: %s, random: %s} -->' % (id(head), head.data, id(head.random)),
	head = head.next
    print 'None'

def FullCopy(head):
    h = head
    while h:
        node = Node(h.data)
	temp = h.next
	h.next = node
	node.next = temp
	h = temp
    h = head
    while h:
        h.next.random = h.random.next
	h = h.next.next
    h = head
    copied = None
    ch = None
    while h:
        t = h.next
	if t is None:
	    break
        h.next = h.next.next
	if not copied:
	    copied = t
	    ch = t
	else:
	    ch.next = t
	    ch = ch.next
    return copied

if __name__ == '__main__':
    # Create List
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # Assign random pointers
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head.next

    print 'Original List'
    PrintList(head)
    print 'Copied List'
    copied = FullCopy(head)
    PrintList(copied)
