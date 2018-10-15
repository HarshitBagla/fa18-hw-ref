"""
matrix_multiply

Given two 2-D input arrays `arr0`, `arr1`, return the matrix product arr0 * arr1.
Return None if the matrix product does not exist.

As with math, assume that indices are in [row][column] format, so each inner list is a row.
"""
def matrix_multiply(arr0, arr1):
	if len(arr0[0]) != len(arr1):
		return None
	prod = []
	for i in range(0,len(arr0)):
		prod.append([])
		for j in range(0,len(arr1[0])):
			prod[i].append(0)
	for i in range(0,len(arr0)):
		for j in range(0,len(arr1[0])):
			for k in range(0,len(arr1)):
				prod[i][j] += arr0[i][k] * arr1[k][j]
	return prod

"""
nth_largest_element

Given an input list `arr`, and index `n`, return the nth largest element.
Avoid using built-in sorting methods.
"""
def pify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        pify(arr, n, largest)

def sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        pify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        pify(arr, i, 0)

def nth_largest_element(arr, n):
	if n >= len(arr):
		return None
	sort(arr)
	return arr[len(arr)-n]

"""
reverse_block

Given an input list `arr`, and a block size `n` > 0, reverse the list in blocks of n.

Example:
	Arguments:
		[1,2,3, 4,5,6, 7], 3
	Return:
		[3,2,1, 6,5,4, 7]
	(spacing added for emphasis)

"""
def reverse_block(arr, n):
	temp = []
	i=0
	while (i+n) < len(arr):
		temp.append(arr[i:i+n])
		i += n
	temp.append(arr[i:])
	for l in temp:
		l.reverse()
	output = []
	for i in range(0, len(temp)):
		for j in range(0, len(temp[i])):
			output.append(temp[i][j])
	return output

"""
subset_sum

Given an input list `arr`, and a number `target`, return whether or not any possible subset of the values in `arr` could sum to `target`.

Example 1:
	Arguments:
		[1,2,3,4,5,7], 13
		7 + 4 + 2 = 13
	Return:
		True

Example 2:
	Arguments:
		[1,2,-1,5,4,-196], 196
	Return:
		False
"""
def subset_sum(arr, target):
	if target is 0:
		return True
	elif len(arr) is 0:
		return False
	else:
		return subset_sum(arr[1:],(target-arr[0])) or subset_sum(arr[1:], target)

"""
spiral_matrix

Given an input 2-D array, return a list with the values obtained by following a clockwise spiral path, starting from [0][0], then proceeding to [0][n], [m][n], [m][0], then going inwards:

Example:
	Argument:
		[[a,b,c,d,e],
		 [f,g,h,i,j],
		 [k,l,m,n,o],
		 [p,q,r,s,t],
		 [u,v,w,x,y]]
	Return:
		[a,b,c,d,e, j,o,t,y, x,w,v,u, p,k,f, g,h,i, n,s, r,q, l, m]
"""
def spiral_matrix(arr):
	output = []
	k=0
	m = len(arr)
	n = len(arr[0])
	x = 0
	while x < m*n:
		for i in range(k,n-k):
			output.append(arr[k][i])
			x += 1
		if x >= m*n:
			break
		for i in range(1+k,m-k):
			output.append(arr[i][n-1-k])
			x += 1
		if x >= m*n:
			break
		for i in range(1+k,n-k):
			output.append(arr[m-1-k][n-1-i])
			x += 1
		if x >= m*n:
			break
		for i in range(1+k,m-1-k):
			output.append(arr[m-1-i][k])
			x += 1
		k += 1
	return output

print(subset_sum([-1,3,-4,6], -3))
