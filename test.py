import asyncio
import unittest
from get_matrix_main import get_matrix, get_matrix_spiral, parse_matrix_from_str


class MyTestCase(unittest.TestCase):
    def test_url_matrix(self):
        SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
        TRAVERSAL = [
            10, 50, 90, 130,
            140, 150, 160, 120,
            80, 40, 30, 20,
            60, 100, 110, 70,
        ]

        self.assertEqual(asyncio.run(get_matrix(SOURCE_URL)), TRAVERSAL)

    def test_spiral_uneven_3(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        answer = [1, 4, 7, 8, 9, 6, 3, 2, 5]
        self.assertEqual(get_matrix_spiral(matrix), answer)

    def test_spiral_uneven_5(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        answer = [
            1, 6, 11, 16, 21, 22, 23, 24, 25, 20, 15, 10, 5, 4, 3, 2, 7, 12, 17, 18, 19, 14, 9, 8, 13
        ]
        self.assertEqual(get_matrix_spiral(matrix), answer)

    def test_spiral_1(self):
        matrix = [[1]]
        answer = [1]
        self.assertEqual(get_matrix_spiral(matrix), answer)

    def test_spiral_even_2(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        answer = [1, 3, 4, 2]
        self.assertEqual(get_matrix_spiral(matrix), answer)

    def test_parsing(self):
        text_matrix = """+-----+-----+-----+-----+
|  10 |  20 |  30 |  40 |
+-----+-----+-----+-----+
|  50 |  60 |  70 |  80 |
+-----+-----+-----+-----+
|  90 | 100 | 110 | 120 |
+-----+-----+-----+-----+
| 130 | 140 | 150 | 160 |
+-----+-----+-----+-----+"""
        answer = [
            [10, 20, 30, 40],
            [50, 60, 70, 80],
            [90, 100, 110, 120],
            [130, 140, 150, 160]
        ]
        self.assertEqual(parse_matrix_from_str(text_matrix), answer)

    def test_url_error_handle(self): # should be test for this but i dont know how to cause
        pass


if __name__ == '__main__':
    unittest.main()
