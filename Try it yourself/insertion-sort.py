

def insertion_sort (A):

	for j in range(1, len(A)):
		key = A[j]
		i = j - 1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key

	return A


list_of_numbers = [5,2,4,6,1,3,5,5,7,8,21]
print("Unordered list of numbers: " + str(list_of_numbers))
print("List of numbers sorted: " + str(insertion_sort(list_of_numbers)))