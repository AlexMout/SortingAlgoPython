import unittest
from sortingalgos import Algorithms

class TestSortingAlgos(unittest.TestCase):
    def setUp(self):
        self.toBeSorted_1 = [10,8,4,2,57,3,2]
        self.sorted_1 = sorted(self.toBeSorted_1)

        self.toBeSorted_2 = [i for i in range(0,20,-1)]
        self.sorted_2 = sorted(self.toBeSorted_2)

    def test_BubbleSort(self):
        print("TEST BUBBLE SORT")
        Algorithms.bubble_sort(self.toBeSorted_1)
        Algorithms.bubble_sort(self.toBeSorted_2)
        self.assertEqual(self.toBeSorted_1,self.sorted_1)
        self.assertEqual(self.toBeSorted_2,self.sorted_2)

    def test_SelectionSort(self):
        print("TEST SELECTION SORT")
        Algorithms.selection_sort(self.toBeSorted_1)
        Algorithms.selection_sort(self.toBeSorted_2)
        self.assertEqual(self.toBeSorted_1,self.sorted_1)
        self.assertEqual(self.toBeSorted_2, self.sorted_2)

    def test_MergeSort(self):
        print("TEST MERGE SORT")
        n1 = len(self.toBeSorted_1)
        n2 = len(self.toBeSorted_2)
        Algorithms.MergeSort(self.toBeSorted_1,0,n1)
        Algorithms.MergeSort(self.toBeSorted_2,0,n2)
        self.assertEqual(self.sorted_1,self.toBeSorted_1)
        self.assertEqual(self.sorted_2, self.toBeSorted_2)

if __name__ == "__main__":
    unittest.main()