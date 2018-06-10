import math

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

    @staticmethod
    def __Merge(arr,l,m,r):
        """
        MERGE FUNCTION FOR MERGESORT
        FIRST ARRAY : arr[l...m] MERGED WITH SECOND : arr[m+1...r]
        """
        arr1_copy = [item for item in arr[l:m+1]]
        arr2_copy = [item for item in arr[m+1:r+1]]

        i=0 #subarray arr1 index
        j=0 #subarray arr2 index
        k=l #original arr index

        #Merging 2 subarray already sorted into a sorted array is O(n):
        while i < len(arr1_copy) and j < len(arr2_copy):
            if arr1_copy[i]<=arr2_copy[j]:
                arr[k]=arr1_copy[i]
                i+=1
            else:
                arr[k]=arr2_copy[j]
                j+=1
            k+=1

        #Copy the rest of the subarray that hasn't been fully copied:
        while i < len(arr1_copy):
            arr[k]=arr1_copy[i]
            i+=1
            k+=1

        while j < len(arr2_copy):
            arr[k]=arr2_copy[j]
            j+=1
            k+=1

    @classmethod
    def MergeSort(cls,arr,l,r):
        """
        MERGE SORT COMPLEXITY IN ANY CASE (WORST,AVG,BEST) IS O(nlog(n))
        DIVIDE AND CONQUER RECURSIVE ALGORITHM
        INPUTS : ARRAY TO BE SORTED, LEFT INDEX, RIGHT INDEX
        """
        if l<r:
            m = int((l+r)/2)
            cls.MergeSort(arr,l,m)
            cls.MergeSort(arr,m+1,r)
            cls.__Merge(arr,l,m,r)

#TODO : Add Quicksort