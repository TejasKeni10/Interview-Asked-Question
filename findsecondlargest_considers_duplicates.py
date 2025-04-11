# lista = [7,8,6,5,7,8,6,89,89,68,8]    #repeate
# biggest = 0
# second_biggest = 0
# for i in range(0,len(lista)):
#     if lista[i] > biggest:
#         biggest = lista[i]
#     if i >= 1:
#         # if max(lista[i-1],second_biggest) != biggest:     for repeated number
#                second_biggest = max(lista[i-1],second_biggest)

            
# print("this is biggest: ",biggest)
# print("this second biggest: ",second_biggest)

import unittest

def findbiggest(lisst):
    biggest  = float('-inf')
    second_biggest = float('-inf')

    for num in lisst:
        if num > biggest:
            second_biggest = biggest
            biggest = num
        elif num > second_biggest and num <= biggest:
            second_biggest = num

    print(f"Biggest: {biggest}, Second Biggest: {second_biggest}")
    return biggest , second_biggest



class Tests(unittest.TestCase):

    def test_all_same_elements(self):
        self.assertEqual(findbiggest([9, 9, 9, 9]), (9, 9))

    def test_two_elements_only(self):
        self.assertEqual(findbiggest([3, 8]), (8, 3))

    def test_descending_order(self):
        self.assertEqual(findbiggest([100, 90, 80, 70]), (100, 90))

    def test_ascending_order(self):
        self.assertEqual(findbiggest([1, 2, 3, 4]), (4, 3))

    def test_negative_duplicates(self):
        self.assertEqual(findbiggest([-1, -1, -2, -3]), (-1, -1))

    def test_negative_only_unique(self):
        self.assertEqual(findbiggest([-10, -20, -30]), (-10, -20))

    def test_large_numbers(self):
        self.assertEqual(findbiggest([1000000, 999999, 888888]), (1000000, 999999))

    def test_zero_included(self):
        self.assertEqual(findbiggest([0, 10, -10]), (10, 0))

    def test_with_floats(self):
        self.assertEqual(findbiggest([1.5, 2.5, 3.5]), (3.5, 2.5))

    def test_mixed_floats_and_ints(self):
        self.assertEqual(findbiggest([1, 2.2, 3, 2.2]), (3, 2.2))

    def test_biggest_duplicate_middle(self):
        self.assertEqual(findbiggest([1, 99, 99, 5]), (99, 99))

    def test_small_list_with_duplicates(self):
        self.assertEqual(findbiggest([4, 4]), (4, 4))

    def test_biggest_last(self):
        self.assertEqual(findbiggest([3, 1, 7]), (7, 3))

    def test_second_biggest_duplicate(self):
        self.assertEqual(findbiggest([9, 6, 9, 6, 5]), (9, 9))

    def test_with_zero_only(self):
        self.assertEqual(findbiggest([0, 0, 0]), (0, 0))

    def test_large_gap(self):
        self.assertEqual(findbiggest([1, 1000000, 2]), (1000000, 2))

    def test_mixed_signs(self):
        self.assertEqual(findbiggest([-100, 0, 100]), (100, 0))

    def test_single_negative(self):
        self.assertEqual(findbiggest([-1]), (-1, float('-inf')))

    def test_many_same_second_largest(self):
        self.assertEqual(findbiggest([8, 8, 9, 9, 10]), (10, 9))

    def test_mixed_extremes(self):
        self.assertEqual(findbiggest([-99999, 99999, 0]), (99999, 0))


if __name__ == '__main__':
    unittest.main()

