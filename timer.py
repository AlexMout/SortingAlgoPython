from sortingalgos import Algorithms
import timeit
import random

toSort = [random.randint(0,1000) for i in range(5000)]

nb_iter = 10

start_time = timeit.default_timer()
for i in range(nb_iter):
    Algorithms.bubble_sort(toSort)
print("Bubble sort average time : {}".format((timeit.default_timer()-start_time)/nb_iter))

print("\n" + "*"*50 + "\n")

start_time = timeit.default_timer()
for i in range(nb_iter):
    Algorithms.selection_sort(toSort)
print("Selection sort average time : {}".format((timeit.default_timer()-start_time)/nb_iter))

print("\n" + "*"*50 + "\n")

start_time = timeit.default_timer()
for i in range(nb_iter):
    Algorithms.MergeSort(toSort,0,len(toSort)-1)
print("Merge sort average time : {}".format((timeit.default_timer()-start_time)/nb_iter))