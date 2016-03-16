class Node(object):
    def __init__(self, data):
        self.data = data
	self.next = None

def Findloop(ll):
    slow = fast = ll
    while slow and fast and fast.next:
        slow = slow.next
	fast = fast.next.next
	if slow == fast:
	    return True
    return False

if __name__ == '__main__':
    ll = Node(1)
    ll.next = Node(2)
    ll.next.next = Node(3)
    ll.next.next.next = Node(4)
    ll.next.next.next.next = Node(5)
    ll.next.next.next.next.next = Node(6)
#    ll.next.next.next.next.next.next = ll.next.next.next

    print Findloop(ll)

