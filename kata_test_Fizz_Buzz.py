import unittest
import kata
#https://docs.python.org/3/library/unittest.html

class TestStringMethods(unittest.TestCase):

    def test_valor_de(self):
        self.assertEqual(kata.valor_de(1),1)
    #
    #def test_divisible_por_3(self):
    #    self.assertEqual(kata.divisible_por_3(3),"fizz")
#
    #def test_divisible_por_5(self):
    #    self.assertEqual(kata.divisible_por_5(5),"buzz")
    #
    #def test_divisible_3_5(self):
    #    self.assertEqual(kata.divisible_3_5(15),"fizz buzz")

    def test_1_1(self):
        self.assertEqual(kata.fizzbuzzer(1), 1)

    def test_2_2(self):
        self.assertEqual(kata.fizzbuzzer(2), 2)

    def test_fizz(self):
        self.assertEqual(kata.fizzbuzzer(3), "Fizz")

    def test_buzz(self):
        self.assertEqual(kata.fizzbuzzer(5), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(kata.fizzbuzzer(15), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()






    