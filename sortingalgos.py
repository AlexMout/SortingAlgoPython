####  PYTHON SORTING ALGOS - MOUTURAT ALEX  ######

# Algo visualization on : visualgo.net

#BUBBLE SORT 
def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)-i-1):
      if(arr[j]>arr[j+1]):
        swap_value(arr,j,j+1)
      #print("liste : a = {} / i = {} / j = {}".format(arr,i,j))

def swap_value(arr,i,j):
  arr[i],arr[j] = arr[j],arr[i]
  
array = [6,4,5,1,8,3,10,9]

#print(array)
#bubble_sort(array)
#print(array)

#SELECTION SORT
def selection_sort(arr):
  for i in range(len(arr)):
    min_index = i
    for j in range(i,len(arr)):
      if arr[min_index]>arr[j]:
        min_index = j
    swap_value(arr,min_index,i)
    print(arr)
    
print(array)
selection_sort(array)
print(array)
