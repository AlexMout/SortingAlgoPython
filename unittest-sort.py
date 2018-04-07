import unittest
from SortingAlgoPython import sortingalgos as algo

class TestSortingAlgos(unittest.TestCase):
    def setUp(self):
        self.toBeSorted_1 = [10,8,4,2,57,3,2]
        self.sorted_1 = sorted(self.toBeSorted_1)

        self.toBeSorted_2 = [i for i in range(0,20,-1)]
        self.sorted_2 = sorted(self.toBeSorted_2)

    def test_BubbleSort(self):
        print("TEST BUBBLE SORT")
        algo.Algorithms.bubble_sort(self.toBeSorted_1)
        algo.Algorithms.bubble_sort(self.toBeSorted_2)
        self.assertEqual(self.toBeSorted_1,self.sorted_1)
        self.assertEqual(self.toBeSorted_2,self.sorted_2)

    def test_SelectionSort(self):
        print("TEST SELECTION SORT")
        algo.Algorithms.selection_sort(self.toBeSorted_1)
        algo.Algorithms.selection_sort(self.toBeSorted_2)
        self.assertEqual(self.toBeSorted_1,self.sorted_1)
        self.assertEqual(self.toBeSorted_2, self.sorted_2)

if __name__ == "__main__":
    unittest.main()