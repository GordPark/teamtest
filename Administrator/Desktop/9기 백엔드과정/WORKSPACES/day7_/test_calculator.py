import unittest
# from calculator import Calculator
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(3,8)
        self.assertEqual(result, 11)
    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(3,8)
        self.assertEqual(result, 24)
    def test_divide(self):
        calc = Calculator()
        result = calc.divide(16,2)
        self.assertEqual(result, 8)


# 수학함수 테스트
class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

# 문자열 반전 함수 테스트
class TestStringFunction(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("likelion"), "noilekil")

# 리스트 정렬 함수
class TestListFunction(unittest.TestCase):
    def test_sort_list(self):
        result = sort_list(['찬희','윤아', '현수', '신혁'])
        self.assertEqual(result, ['신혁', '윤아', '찬희', '현수' ])

# 사용자 정의 클래스 메서드 테스트
class TestPersonClass(unittest.TestCase):
    def test_is_adult(self):
        adult = Person('John', 19)
        self.assertTrue(adult.is_adult())

# 예외 발생 테스트
class TestException(unittest.TestCase):
    def test_exception(self):
        with self.assertRaises(ValueError):
            divide_new(10, 0)

class TestFileOperations(unittest.TestCase):
    def test_write_to_file(self):
        write_to_file("test.txt", "hello world")
        with open("test.txt," 'r') as f:
            self.assertEqual(f.read(), 'hello world')

if __name__=="__main__":
    unittest.main()