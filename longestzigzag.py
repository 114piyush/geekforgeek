
def FindMaxLenghtZigZag(arr):
    # Base case
    if not len(arr):
        return 0
    elif len(arr) == 1:
        return 1

    max_len = max_so_far = 1
    flag = None
    # Initialize flag based on initial 2 values
    # Case when some first values are equall
    i = 1
    while arr[i-1] == arr[i]:
        i += 1
    if arr[i-1] < arr[i]:
        flag = False
    else:
        flag = True

    for j in range(i, len(arr)):
        if arr[j-1] < arr[j] and not flag:
	    max_so_far += 1
	    flag = True
	elif arr[j-1] > arr[j] and flag:
	    max_so_far += 1
	    flag = False
	else:
	    if max_len < max_so_far:
	        max_len = max_so_far
		max_so_far = 1
		# Reinitialize falg
	    while j < len(arr) and arr[j-1] == arr[j]:
	        j += 1
	    if arr[j-1] < arr[j]:
	        flag = False
	    else:
	        flag = True
    # Last case
    if max_len < max_so_far:
        max_len = max_so_far

    return max_len

if __name__ == '__main__':
    arr = map(int, raw_input().split())
    print FindMaxLenghtZigZag(arr)
