import unittest

from sort_tri import trier

class TestBubbleSort(unittest.TestCase):
    # Testez une liste vide
    def test_bubble_sort_empty_list(self):
        unsorted_list = []
        expected_output = []
        self.assertEqual(trier(unsorted_list), expected_output)
    # Testez une liste de longueur 1
    def test_bubble_sort_single_item_list(self):
        unsorted_list = [1]
        expected_output = [1]
        self.assertEqual(trier(unsorted_list), expected_output)

    #Testez une liste déjà triée dans l'ordre décroissant
    def test_bubble_sort_reverse_ordered_list(self):
        unsorted_list = [3, 2, 1]
        expected_output = [1, 2, 3]
        self.assertEqual(trier(unsorted_list), expected_output)

    #Testez une liste avec des valeurs nulles
    def test_bubble_sort_list_with_zeros(self):
        unsorted_list = [5, 0, 3, 0, 1]
        expected_output = [0, 0, 1, 3, 5]
        self.assertEqual(trier(unsorted_list), expected_output)

    #Testez une liste avec des valeurs en double et des doublons
    def test_bubble_sort_list_with_duplicates(self):
        unsorted_list = [5, 2, 3, 2, 1]
        expected_output = [1, 2, 2, 3, 5]
        self.assertEqual(trier(unsorted_list), expected_output)

    #Testez une liste avec des nombres négatifs
    def test_bubble_sort_list_with_negatives(self):
        unsorted_list = [-5, 0, 3, -2, 1]
        expected_output = [-5, -2, 0, 1, 3]
        self.assertEqual(trier(unsorted_list), expected_output)

if __name__ == '__main__':
    unittest.main()
