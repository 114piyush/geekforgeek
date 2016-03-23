def Spiral(arr, m, n):
    # Start point
    i = j = 0
    while i!=m and j!=n:
        # Print row
        row = i
        for t in range(j, n):
            print arr[row][t],
        # Print column
        col = t
        for t in range(i+1, m):
            print arr[t][col],
        # Print row
        row = t
	#print 'row:%d col:%d' % (row, col)
        for t in range(col-1, j-1, -1):
	    #print 'test'
            print arr[row][t],
        col = t
	#print 'row:%d col:%d' % (row, col)
        # Print column
        for t in range(row-1, i, -1):
            print arr[t][col],
        row = t
	#print 'row:%d col:%d' % (row, col)
        # Decrement m and n
        m -= 1
        n -= 1
        # Change starting point
        i = row
        j = col+1

def RecSpiral(arr, i, j, m, n):
    #print "Row:%d col:%d m:%d, n:%d" % (i, j, m, n)
    if i == m-1 and j == n-1:
        print arr[i][j],
        return
    row = i
    # Print row
    for t in range(j, n):
        print arr[row][t],
    col = t
    # Print column
    for t in range(i+1, m):
        print arr[t][col],
    row = t
    # Print row
    for t in range(col-1, j-1, -1):
        print arr[row][t],
    col = t
    # Print column
    for t in range(row-1, i, -1):
        print arr[t][col],
    row = t
    i = row
    j = col+1
    m -= 1
    n -= 1
    RecSpiral(arr, i, j, m, n)

def Print(arr, m, n):
    for i in range(m):
        for j in range(n):
	    print arr[i][j],
	print

def isvalid(i, j, m, n):
    if i < 0 or i >= m or j < 0 or j >= n:
        return False
    return True

def DiagonalOrder(arr, m, n):
    #-------------------------
    #1  2  3  4  5
    #6  7  8  9  10
    #11 12 13 14 15
    #-------------------------
    # Output: 1, 6 2, 11 7 3, 12 8 4, 13 9 5, 14 10, 15
    # Formula:
    # Total antidigonals = m+n-1
    for i in range(m+n-1):
        if i < m:
	    row = i
	    col = 0
	else:
	   row = m-1
	   col = i+1-m
	while isvalid(row, col):
	    print arr[row][col],
	    row -= 1
	    col += 1
	print

def DiagonalZigZag(arr, m, n):
    flag = False
    for i in range(m+n-1):
        if not flag:
	    if i < m:
	        row = i
		col = 0
	    else:
	        row = m-1
		col = i+1-m
	    while isvalid(row, col, m, n):
	        print arr[row][col],
		row -= 1
		col += 1
	else:
	    if i < n:
	        row = 0
		col = i
	    else:
	        col = n-1
		row = i+1-n
	    while isvalid(row, col, m, n):
	        print arr[row][col],
		row += 1
		col -= 1
	print
	flag = not flag

if __name__ == '__main__':
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    Print(arr, 3, 3)
    Spiral(arr, 3, 3)
    RecSpiral(arr, 0, 0, 3, 3)
    DiagonalOrder(arr, 3, 3)
    DiagonalZigZag(arr, 3, 3)
