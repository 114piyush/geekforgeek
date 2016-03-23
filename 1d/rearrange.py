def max_min(arr, n):
    """
    Input:  0 1 2 3 4 5 6
    Output: 6 0 5 1 4 2 3
    Logic: Try to see some pattern
    Algo:
    1. Find index to keep in proper place
    2. Save value at index
    3. Put element in current and mark as negative
    Limitation: works only for positive numbers
    """
    for j in range(n):
       if arr[j] < 0:
	   continue
       i = j
       curr = arr[i]
       while curr > 0:
           if i < n/2:
               index = 2*i+1
	   else:
	       index = n-1 - (2*i+1)%n
           temp = arr[index]
           arr[index] = -curr
           curr = temp
           i = index
    return map(lambda x: -x, arr)


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7]
    print a
    print max_min(a, len(a))
