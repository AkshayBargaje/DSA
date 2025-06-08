# first pattern in binary search

# This is the recursion way of doing it
# considerations that the array is sorted in the acending order
def search(arr,n,left,right):
	if left > right:
		return 
	mid =int(left +(right - left)/2)   # This is done because (left+ right) might give overflow issue  
	if(arr[mid]==n):
		return mid
	elif(arr[mid] > n):
		# right = mid-1
		# the element is in left part of the array
		return search(arr,n,left,mid-1)
	else:
		# left = mid+1
		# the element is in left part of the array
		return search(arr,n,mid+1,right)


# iterative way for the binary search
# consideration acending order array
def itBinarySearch(arr,n):
	left = 0
	right = len(arr)-1
	while(left < right):
		mid = int(left+(right-left)/2)
		if(arr[mid]==n):
			return mid
		elif(arr[mid] > n):
			right = mid-1
			# the element is in left part of the array
		else:
			left = mid+1
			# the element is in left part of the array

def itorderAgnosticBinarySearch(arr,n):
	left = 0
	right = len(arr)-1
	isAsc = True if arr[left]<arr[right] else False
	while(left < right):
		mid = int(left+(right-left)/2)
		if(arr[mid]==n):
			return mid
		elif isAsc:
			if(arr[mid] > n):
				right = mid-1
				# the element is in left part of the array
			else:
				left = mid+1
				# the element is in left part of the array
		else:
			if(arr[mid] < n):
				right = mid-1
				# the element is in left part of the array
			else:
				left = mid + 1
				# the element is in left part of the array


# here athe array will be sort but the order of sorting is unknown
def orderAgnosticBinarySearch(arr,n,left,right):
	mid = int(left + (right -left)/2)

	if left > right:
		return

	if arr[mid] == n:
		return mid
	# elif arr[left] < arr[right] && arr[mid] < n:  # In case of acending and element small
	# 	return orderAgnosticBinarySearch(arr,n,mid+1,right)

	# elif arr[left] < arr[right] && arr[mid] > n:  # In case of acending and element greater
	# 	return orderAgnosticBinarySearch(arr,n,left,mid-1)

	# elif arr[left] > arr[right] && arr[mid] < n:  # In case of decending and element small
	# 	return orderAgnosticBinarySearch(arr,n,left,mid-1)

	# else:                              			#In case of decending and element greater
	# 	return orderAgnosticBinarySearch(arr,n,mid+1,right)

	# -------------------By observing the function calls we can optimize the conditions
	elif (arr[left] < arr[right] and arr[mid] > n) or (arr[left] > arr[right] and arr[mid] < n):
		return orderAgnosticBinarySearch(arr,n,left,mid-1)
	else:                              			
		return orderAgnosticBinarySearch(arr,n,mid+1,right)


# This is for searching in a 2d matrix
# here trick is 
# row  = i //cols
# col = i % cols
def searchMatrix(self, matrix, target):
    n = len(matrix[0] * len(matrix))
    cols = len(matrix)
	left = 0
    right = len(arr)-1
    while(left < right):
	    mid = int(left+(right-left)/2)
	    if(matrix[mid//cols][mid % cols]==n):
		    return mid
   		elif(matrix[mid//cols][mid % cols] > n):
    		right = mid-1
	    	# the element is in left part of the array
	    else:
		    left = mid+1
		    # the element is in left part of the array

def main():
	print(search([1,2,3,4,5,6,7],6,0,6))
	print(itBinarySearch([1,2,3,4,5,6,7],6))
	print(itorderAgnosticBinarySearch([1,2,3,4,5,6,7],6))
	print(orderAgnosticBinarySearch([1,2,3,4,5,6,7],6,0,6))
	print(orderAgnosticBinarySearch([7,6,5,4,3,2,1],6,0,6))



if __name__ == '__main__':
	main()