def countSetBits(num):
    count = 0
    while num:
        num &= (num - 1)
	count += 1
    return count

def isPower2(num):
    if countSetBits(num) == 1:
         return True
    return False

if __name__ == '__main__':
    print isPower2(1)
    print isPower2(2)
    print isPower2(3)
    print isPower2(4)
    print isPower2(5)
    print isPower2(8)
    print isPower2(2**16)
