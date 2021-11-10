from typing import List, Optional, Callable


def siftdown_max(a: List, length: int, root: int) -> None:
	"""
	Heapifying a list in a siftdown manner using recursion sorting list from largest to smallest. Modifies original list pass to function
	Args:
	 :param root: the index of the current node we are looking at
	 :param length: length of the heap list
	 :param a: list that is build as a heap
	"""
	left = 2 * root + 1   # The left child to root
	right = 2 * root + 2  # The right child to root
	largest = root        # Holds index to largest element

	# Checks if child isn't out of bound, then it its larger
	if left < length and a[left] < a[largest]:
		largest = left
	if right < length and a[right] < a[largest]:
		largest = right

	if largest != root:
		a[root], a[largest] = a[largest], a[root]
		siftdown_max(a, length, largest)


def siftdown_min(a: List, length: int, root: int) -> None:
	"""
	Heapifying a list in a siftdown manner using recursion sorting list from smallest to largest.
	Modifies original list pass to function
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
		siftdown_min(a, length, largest)


def siftdownItter_max(a: List, length: int, root: int) -> None:
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
		if left < length and a[left] < a[largest]:
			largest = left
		if right < length and a[right] < a[largest]:
			largest = right

		if largest == root:
			break

		a[root], a[largest] = a[largest], a[root]
		root = largest


def buildHeap(a: List, size: int, sifter):
	""" Builds a max heap from a given list """
	# Start from the middle index and moves towards 0
	for i in range((size // 2), -1, -1):
		sifter(a, size, i)


def heap_sort(
		a: Optional[List] = None,
		sifter: Optional[Callable[[List[int], int, int], None]] = siftdown_max):
	"""
	Heapifying a list in a siftdown manner using recursion. Modifies original list pass to function
	Args:
	 :param a: The optional list that's to be sorted. Will return a function with the sifter set if no list is provided
	 :param sifter: The function that fixes the heap, uses siftdown_max by default
	"""
	def inner(a: List):
		n = len(a)
		buildHeap(a, n, sifter)
		for i in range(n - 1, 0, -1):
			a[i], a[0] = a[0], a[i]
			sifter(a, i, 0)

	return inner(a) if a else inner

