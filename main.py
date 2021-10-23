import random
import time

from heapsort import head_sort


def main():
	n = 100000
	rand_list = [random.randrange(0, 100) for _ in range(0, n)]

	start = time.process_time()
	head_sort(rand_list)
	end = time.process_time()
	print(f"time used: {end - start}")


if __name__ == '__main__':
	main()
