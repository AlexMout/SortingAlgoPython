from SortingAlgoPython import sortingalgos
import timeit
import random

toSort = [random.randint(0,1000) for i in range(500)]

start_time = timeit.default_timer()
for i in range(1000):
    sortingalgos.Algorithms.bubble_sort(toSort)
print("Bubble sort average time : {}".format((timeit.default_timer()-start_time)/1000))

print("\n" + "*"*50 + "\n")

start_time = timeit.default_timer()
for i in range(1000):
    sortingalgos.Algorithms.selection_sort(toSort)
print("Selection sort average time : {}".format((timeit.default_timer()-start_time)/1000))