import unittest
from final import slide, shift, encrypt, file_away, raise_to_power
from final import is_missing, equal_stacks
from Stack import Stack


class TestFunctions(unittest.TestCase):

    def test_slide(self):
        self.assertEqual("Hello", slide("Hello", 0))
        self.assertEqual("loHel", slide("Hello", 2))
        self.assertEqual("oHell", slide("Hello", 6))
        self.assertEqual("elloH", slide("Hello", -1))
        self.assertEqual("braZe", slide("Zebra", -2))
        self.assertEqual("e carRac", slide("Race car", 5))
        self.assertEqual("Hello", slide("Hello", 10))

    def test_shift(self):
        self.assertEqual("HELLO", shift("HELLO", 0))
        self.assertEqual("HELLO", shift("hello", 0))
        self.assertEqual("HELLO", shift("HELLO", -1))
        self.assertEqual("dOL\K", shift("Zebra", 10))
        self.assertEqual("`KHXG", shift("ZEBRA", 6))
        self.assertEqual("aPRT RPa", shift("Race car", 15))
        self.assertEqual("HELLO", shift("Hello", 16))

    def test_function_object(self):
        self.assertEqual("`KHXG", encrypt(shift, "ZEBRA", 6))
        self.assertEqual("e carRac", encrypt(slide, "Race car", 5))

    def test_file(self):
        d = {'Shakespeare': 'All that glitters is not gold\n', 'Jesus': 'For unto whomsoever much is given, of him shall be much required\n', 'Stan Lee': 'With great power comes great responsibility\n', 'Terminator': "I'll be back\n", 'Forrest Gump': 'Life is like a box of chocolates\n', 'Nelson Mandela': 'The greatest glory in living lies not in never falling, but in rising every time we fall\n', 'Mahatma Ghandi': 'You must be the change you wish to see in the world\n', 'Martin Luther King, Jr.': 'Darkness cannot drive out darkness: only light can do that. Hate cannot drive out hate: only love can do that\n', 'Oscar Wilde': 'Be yourself; everyone else is already taken\n', 'Prof Keith': 'Have a great Winter Break! See you next semester!'}
        self.assertEqual(d, file_away("quotes.txt"))
        d = {'The Thing': "It's clobberin' time!\n", 'Superman': 'Up, up and away!\n', 'Robin': 'Holy deep fried pizza, Batman!\n', 'Spider-Man': 'Just your friendly neighborhood Spider-Man!'}
        self.assertEqual(d, file_away("super.txt"))
        self.assertEqual({}, file_away("misquotes.txt"))

    def test_raise_to_power(self):
        self.assertEqual(2**4, raise_to_power(2, 4))
        self.assertEqual(3**3, raise_to_power(3, 3))
        self.assertEqual(10**2, raise_to_power(10, 2))
        self.assertEqual(10**0, raise_to_power(10,0))
        self.assertEqual((-2)**2, raise_to_power(-2, 2))

    def test_is_missing(self):
        self.assertEqual(is_missing([2,3,4]), 1)
        self.assertEqual(is_missing([4,1,3,6,7,2]), 5)
        self.assertEqual(is_missing([4,1,3]), 2)
        self.assertEqual(is_missing([1]), 2)

    def test_equal_stacks(self):
        s1 = Stack()
        s1.push(1)
        s1.push(2)

        s2 = Stack()
        s2.push(1)
        s2.push(2)
        self.assertEqual(equal_stacks(s1, s2), True)

        s1 = Stack()
        s1.push(1)
        s1.push(2)

        s2 = Stack()
        s2.push(1)
        s2.push(2)
        s2.push(3)
        s2.pop()
        self.assertEqual(equal_stacks(s1, s2), True)

        s1 = Stack()
        s1.push("Hello")
        s1.push("World")

        s2 = Stack()
        s2.push("World")
        s2.push("Hello")

        self.assertEqual(equal_stacks(s1, s2), False)

        s1 = Stack()
        s2 = Stack()
        self.assertEqual(equal_stacks(s1, s2), True)


if __name__ == "__main__":
    unittest.main(verbosity=3)

