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
        elif num > second_biggest and num == biggest:
            second_biggest = num

    print(f"Biggest: {biggest}, Second Biggest: {second_biggest}")
    return biggest , second_biggest



class Tests(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(findbiggest([7, 8, 6, 5, 7, 8, 6, 89, 89, 68, 8]), (89, 68))


    def test_no_second_biggest(self):
        self.assertEqual(findbiggest([5, 5, 5, 3]), (5, 3))

    def test_sorted_list(self):
        self.assertEqual(findbiggest([1, 2, 3, 4, 5]), (5, 4))

    def test_unsorted_with_negatives(self):
        self.assertEqual(findbiggest([-10, -20, 0, 5, -1]), (5, 0))

    def test_single_element(self):
        self.assertEqual(findbiggest([42]), (42, float('-inf')))

    def test_empty_list(self):
        self.assertEqual(findbiggest([]), (float('-inf'), float('-inf')))

if __name__ == '__main__':
    unittest.main()

