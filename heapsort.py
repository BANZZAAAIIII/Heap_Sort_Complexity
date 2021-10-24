from typing import List


def siftdown(a: List, length: int, root: int) -> None:
	"""
	Heapifying a list in a siftdown manner using recursion. Modifies original list pass to function
	Args:
	 :param root: the index of the current node we are looking at
	 :param length: length of the heap list
	 :param a: list that is build as a heap
	"""
	left = 2 * root + 1   # The left child to root
	right = 2 * root + 2  # The right child to root
	largest = root        # Holds index to largest element

	# Checks if child isn't out of bound, then it its larger
	if left < length and a[left] > a[largest]:
		largest = left
	if right < length and a[right] > a[largest]:
		largest = right

	if largest != root:
		a[root], a[largest] = a[largest], a[root]
		siftdown(a, length, largest)


def siftdownItter(a: List, length: int, root: int) -> None:
	"""
	Heapifying a list in a siftdown manner using recursion. Modifies original list pass to function
	Args:
	 :param root: the index of the current node we are looking at
	 :param length: length of the heap list
	 :param a: list that is build as a heap
	"""
	while True:
		left = 2 * root + 1  # The left child to root
		right = 2 * root + 2  # The right child to root
		largest = root  # Holds index to largest element

		# Checks if child isn't out of bound, then it its larger
		if left < length and a[left] > a[largest]:
			largest = left
		if right < length and a[right] > a[largest]:
			largest = right

		if largest == root:
			break

		a[root], a[largest] = a[largest], a[root]
		root = largest


def buildHeap(a: List, size: int):
	""" Builds a max heap from a given list """
	# Start from the middle index and moves towards 0
	for i in range((size // 2), -1, -1):
		siftdown(a, size, i)


def heap_sort(a: List):
	n = len(a)
	buildHeap(a, n)
	for i in range(n - 1, 0, -1):
		a[i], a[0] = a[0], a[i]
		siftdown(a, i, 0)


def main():
	blarg = [2, 8, 1, 4, 14, 7, 16, 10, 9, 3]
	print(f"Sorting: {blarg}")
	heap_sort(blarg)
	print(f"Sorted: {blarg}")


if __name__ == '__main__':
	main()

