import random
import time
from typing import List, Callable, Optional

from matplotlib import pyplot as plt

from heapsort import heap_sort


def random_list(
		sorting: Optional[Callable[[List[int]], List[int]]] = None,
		r_start: int = 0,
		r_end: int = 100
) -> Callable[[int], List[int]]:
	def inner1(size: int) -> List[int]:
		return [random.randrange(r_start, r_end) for _ in range(0, size)]

	def inner2(size: int) -> List[int]:
		r = [random.randrange(r_start, r_end) for _ in range(0, size)]
		heap_sort(r)
		return r

	if sorting is None:
		return inner1
	else:
		return inner2


def get_element_list(step: int = 10000, end: int = 500001):
	start = step
	return [_ for _ in range(start, end, step)]


def sort_blarg(
		sort_sizes: List[int],
		rand_function: Callable[[int], List[int]],
		plotting: Optional[str] = None
) -> List[int]:
	# Holds all times for n
	result = [[] for _ in range(0, len(sort_sizes))]

	for _ in range(0, 5):
		for i, n in enumerate(sort_sizes):
			rand_list = rand_function(n)
			start = time.perf_counter()
			heap_sort(rand_list)
			end = time.perf_counter()
			result[i].append(end - start)

	avg_result = []
	for r in result:
		avg_result.append(sum(r) / len(r))

	if plotting:
		# Converts results to hold list that are a run from start to end
		unzipped_results = list(zip(*result))
		for r in unzipped_results:
			plt.plot(sort_sizes, r, color='cornflowerblue')

		plt.plot(sort_sizes, avg_result, color="red", label='Average')

		plt.grid()
		plt.legend()
		plt.title(plotting)
		plt.xlabel("Number of elements")
		plt.ylabel("Time in seconds")

		plt.show()

	return avg_result


def main():
	nrElements = get_element_list()

	random_values = random_list()
	avg_random = sort_blarg(nrElements, random_values, "Heapsort random values")

	random_values = random_list(sorting=heap_sort)
	avg_sorted = sort_blarg(nrElements, random_values, "Heapsort sorted values")


	# Plotting
	plt.plot(nrElements, avg_random, color="red", label='Random')
	plt.plot(nrElements, avg_sorted, color="blue", label='Sorted')

	plt.grid()
	plt.legend()
	plt.title("Time comparison between types of lists")
	plt.xlabel("Number of elements")
	plt.ylabel("Time in seconds")

	plt.show()


if __name__ == '__main__':
	main()
