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
        elif num > second_biggest and num != biggest:
            second_biggest = num

    print(f"Biggest: {biggest}, Second Biggest: {second_biggest}")
    return biggest , second_biggest



class Tests(unittest.TestCase):

    def test_normal_case(self):
        result = findbiggest([7, 8, 6, 5, 7, 8, 6, 89, 89, 68, 8])
        print("Normal case result:", result)
        self.assertEqual(result, (89, 68))

    def test_no_second_biggest(self):
        result = findbiggest([5, 5, 5, 3])
        print("No second biggest result:", result)
        self.assertEqual(result, (5, 3))

    def test_sorted_list(self):
        result = findbiggest([1, 2, 3, 4, 5])
        print("Sorted list result:", result)
        self.assertEqual(result, (5, 4))

    def test_unsorted_with_negatives(self):
        result = findbiggest([-10, -20, 0, 5, -1])
        print("Unsorted with negatives result:", result)
        self.assertEqual(result, (5, 0))

    def test_single_element(self):
        result = findbiggest([42])
        print("Single element result:", result)
        self.assertEqual(result, (42, float('-inf')))

    def test_empty_list(self):
        result =findbiggest([])
        print("Empty list result:", result)
        self.assertEqual(result, (float('-inf'), float('-inf')))

if __name__ == '__main__':
    unittest.main()

