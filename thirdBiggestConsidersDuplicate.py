import unittest
def third(lisst):
    biggest = float('-inf')
    second = float('-inf')
    third = float('-inf')

    for i in lisst :
        if i > biggest :
            third = second
            second = biggest
            biggest = i

        elif i > second and i <=biggest:
            third = second
            second = i
        elif i > third and i <=second and i <= biggest:
            third = i

    return biggest, second, third



class Tests(unittest.TestCase):

    def test_all_same_elements(self):
        result = third([9, 9, 9, 9])
        print("All same elements:", result)
        self.assertEqual(result, (9, 9, 9))

    def test_descending_order(self):
        result = third([100, 99, 98, 97])
        print("Descending order:", result)
        self.assertEqual(result, (100, 99, 98))

    def test_ascending_order(self):
        result = third([10, 20, 30, 40, 50])
        print("Ascending order:", result)
        self.assertEqual(result, (50, 40, 30))

    def test_two_elements_only(self):
        result = third([4, 9])
        print("Two elements only:", result)
        self.assertEqual(result, (9, 4, float('-inf')))

    def test_duplicates_mixed_in(self):
        result = third([4, 4, 6, 2, 6, 1])
        print("Duplicates mixed in:", result)
        self.assertEqual(result, (6, 6, 4))

    def test_negatives_only(self):
        result = third([-1, -3, -2, -5, -1])
        print("Negatives only:", result)
        self.assertEqual(result, (-1, -1, -2))

    def test_large_numbers(self):
        result = third([1_000_000, 999_999, 2_000_000, 1_500_000])
        print("Large numbers:", result)
        self.assertEqual(result, (2_000_000, 1_500_000, 1_000_000))

    def test_zero_in_list(self):
        result = third([0, -1, -2, -3, 1])
        print("Zero in list:", result)
        self.assertEqual(result, (1, 0, -1))

    def test_with_floats(self):
        result = third([1.5, 2.5, 3.5])
        print("With floats:", result)
        self.assertEqual(result, (3.5, 2.5, 1.5))

    def test_mixed_ints_floats(self):
        result = third([1, 2.5, 3, 2.5])
        print("Mixed ints and floats:", result)
        self.assertEqual(result, (3, 2.5, 2.5))

    def test_third_equal_to_first(self):
        result = third([4, 2, 3, 4])
        print("Third equal to first:", result)
        self.assertEqual(result, (4, 4, 3))

    def test_many_small_numbers(self):
        result = third([1]*1000)
        print("Many small same numbers:", result)
        self.assertEqual(result, (1, 1, 1))

    def test_big_jump_between_numbers(self):
        result = third([1, 1000, 10])
        print("Big jump between numbers:", result)
        self.assertEqual(result, (1000, 10, 1))

    def test_large_list_random(self):
        result = third(list(range(10000)))
        print("Large range list:", result)
        self.assertEqual(result, (9999, 9998, 9997))

    def test_third_number_is_duplicate(self):
        result = third([8, 6, 6, 5, 7])
        print("Third number is duplicate:", result)
        self.assertEqual(result, (8, 7, 6))

    def test_list_with_zeros(self):
        result = third([0, 0, 0, 1])
        print("List with zeros:", result)
        self.assertEqual(result, (1, 0, 0))

    def test_mixed_sign_numbers(self):
        result = third([-10, 0, 10, -5])
        print("Mixed sign numbers:", result)
        self.assertEqual(result, (10, 0, -5))

    def test_large_negative_gap(self):
        result = third([-1_000_000, -2_000_000, -3_000_000])
        print("Large negative gap:", result)
        self.assertEqual(result, (-1_000_000, -2_000_000, -3_000_000))

    def test_only_two_unique_values(self):
        result = third([3, 3, 4, 4])
        print("Only two unique values:", result)
        self.assertEqual(result, (4, 4, 3))

    def test_random_placement(self):
        result = third([5, 1, 5, 9, 9, 4])
        print("Random placement of top values:", result)
        self.assertEqual(result, (9, 9, 5))
if __name__ == '__main__':
    unittest.main()

