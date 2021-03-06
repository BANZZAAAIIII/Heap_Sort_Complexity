# Built in
import random
import time
from math import log, log2
from typing import List, Callable, Optional

# Libraries
from matplotlib import pyplot as plt

# Local
import heapsort as hs
from heapsort import heap_sort


def random_list(
		sort: Optional[Callable[[List[int]], List[int]]] = None,
		r_start: int = 0,
		r_end: int = 100
) -> Callable[[int], List[int]]:
	def random_numbers(size: int) -> List[int]:
		return [random.randrange(r_start, r_end) for _ in range(0, size)]

	def sorted_numbers(size: int) -> List[int]:
		r = [random.randrange(r_start, r_end) for _ in range(0, size)]
		sort(r)
		return r

	return random_numbers if not sort else sorted_numbers


def get_element_list(step: int = 1000, end: int = 10000) -> List[int]:
	start = step
	end = end + 1  # To make the end inclusive
	return [_ for _ in range(start, end, step)]


def sorting(
		repeat_size: int,
		sort_sizes: List[int],
		rand_function: Callable[[int], List[int]],
		plotting: Optional[str] = None,
		in_nano: bool = False
) -> List[int]:
	result = [[] for _ in range(0, len(sort_sizes))]

	timer = time.perf_counter_ns if in_nano else time.perf_counter

	for _ in range(0, repeat_size):
		for i, n in enumerate(sort_sizes):
			rand_list = rand_function(n)
			start = timer()
			heap_sort(rand_list)
			end = timer()
			result[i].append(end - start)

	avg_result = []
	for r in result:
		avg_result.append(sum(r) / len(r))

	if plotting:
		# Converts results to hold list that are a run from start to end
		unzipped_results = list(zip(*result))
		for r in unzipped_results:
			plt.plot(sort_sizes, r, color='lavender')

		plt.plot(sort_sizes, avg_result, color="salmon", label='Average')

		plt.grid()
		plt.legend()
		plt.title(plotting)
		plt.xlabel("Number of elements")
		if in_nano:
			plt.ylabel("Time in nano seconds")
		else:
			plt.ylabel("Time in seconds")

		plt.show()

	return avg_result


def main():
	nrElements = get_element_list(25,  1000)
	repeats = 25
	in_ns = True

	avg_random = sorting(
		repeats,
		nrElements,
		random_list(),
		# "Heapsort random values",
		in_nano=in_ns
	)

	avg_sorted = sorting(
		repeats,
		nrElements,
		random_list(sort=heap_sort),
		# "Heapsort sorted values",
		in_nano=in_ns
	)

	avg_sorted_rev = sorting(
		repeats,
		nrElements,
		random_list(sort=heap_sort(sifter=hs.siftdown_min)),
		# "Heapsort reverse sorted values",
		in_nano=in_ns
	)


	values = [n*log(n) for n in nrElements]

	# Plotting
	_, axes1 = plt.subplots()

	line1 = axes1.plot(nrElements, avg_random, color="salmon", label='Random')
	line2 = axes1.plot(nrElements, avg_sorted, color="tan", label='Sorted')
	line3 = axes1.plot(nrElements, avg_sorted_rev, color="lightgreen", label='Reverse sorted')
	if in_ns:
		axes1.set_ylabel("Time in nano seconds")
	else:
		axes1.set_ylabel("Time in seconds")

	axes1.grid()

	# Creates new twin axes to use in the same graph
	axes2 = axes1.twinx()
	line4 = axes2.plot(nrElements, values, color="slategrey", label='nlogn')
	axes2.axes.get_yaxis().set_visible(False)  # Hides numbers from yaxis

	# Creates common legend for both axis
	all_lines = line1 + line2 + line3 + line4
	all_labels = (label.get_label() for label in all_lines)
	axes1.legend(all_lines, all_labels)

	# Makes plots in axes2 appear behind
	axes1.set_zorder(axes2.get_zorder() + 1)
	axes1.patch.set_visible(False)

	plt.title("Time comparison between types of lists")
	plt.xlabel("Number of elements")
	plt.show()


if __name__ == '__main__':
	main()
