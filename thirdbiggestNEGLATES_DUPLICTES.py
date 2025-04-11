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

        elif i > second and i !=biggest:
            third = second
            second = i
        elif i > third and i !=second and i !=biggest:
            third = i

    return biggest, second, third



class Tests(unittest.TestCase):

    def test_normal_case(self):
        result = third([7, 8, 6, 5, 7, 8, 6, 89, 89, 68, 8])
        print("Normal case:", result)
        self.assertEqual(result, (89, 68, 8))

    def test_no_second_biggest(self):
        result = third([5, 5, 5, 3])
        print("No second biggest:", result)
        self.assertEqual(result, (5, 3, float('-inf')))

    def test_sorted_list(self):
        result = third([1, 2, 3, 4, 5])
        print("Sorted list:", result)
        self.assertEqual(result, (5, 4, 3))

    def test_unsorted_with_negatives(self):
        result = third([-10, -20, 0, 5, -1])
        print("With negatives:", result)
        self.assertEqual(result, (5, 0, -1))

    def test_single_element(self):
        result = third([42])
        print("Single element:", result)
        self.assertEqual(result, (42, float('-inf'), float('-inf')))

    def test_empty_list(self):
        result = third([])
        print("Empty list:", result)
        self.assertEqual(result, (float('-inf'), float('-inf'), float('-inf')))

if __name__ == '__main__':
    unittest.main()

