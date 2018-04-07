####  PYTHON SORTING ALGOS - MOUTURAT ALEX  ######

# Algo visualization on : visualgo.net

class Algorithms:
    @staticmethod
    def __swap_value(arr, i, j):
        """ Method that swaps values in array given the array and the two indices """
        arr[i], arr[j] = arr[j], arr[i]

    @classmethod
    def bubble_sort(cls, arr):
        """ BUBBLE SORT ALGORITHM - Complexy O(n^2) """
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if (arr[j] > arr[j + 1]):
                    cls.__swap_value(arr, j, j + 1)
                # print("liste : a = {} / i = {} / j = {}".format(arr,i,j))

    @classmethod
    def selection_sort(cls,arr):
        """ SELECTION SORT ALGORITMH - Complexy O(n^2) """
        for i in range(len(arr)):
            min_index = i
            for j in range(i, len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j
            cls.__swap_value(arr, min_index, i)

#TODO : Add Merge sort, Quicksort