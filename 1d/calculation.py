def find_pair(arr, x):
    arr = sorted(arr)
    i = 0
    j = len(arr) -1
    while (i < j):
        _sum = arr[i] + arr[j]
        if _sum == x:
	     return arr[i], arr[j]
	elif _sum > x:
	     j -= 1
	else:
	     i += 1
def find_majority(arr):
    """
    Algo: In O(n)
    """
    count = 1
    maj = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == maj:
	    count += 1
	if count == 0:
	    maj = arr[i]
	    count = 1
    if count > len(arr)/2:
        return maj
    else:
        return None

def largest_contiguous_sum(arr):
    n = len(arr)
    max_so_far = 0
    max_ending_here = 0
    for e in arr:
        max_ending_here += e
        if max_ending_here < 0:
	    max_so_far = 0
	if max_so_far < max_ending_here:
	    max_so_far = max_ending_here
    return max_so_far

if __name__ == '__main__':
    arr = [4,56,4,4,3,4,77,]
    print find_pair(arr, 81)
    print find_majority(arr)
    print largest_contiguous_sum(arr)
