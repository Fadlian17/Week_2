# unittest
import unittest


class TestMethod(unittest.TestCase):
    pass

    def tes_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def tes_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def tes_split(self):
        t = 'hello world'
        self.assertEqual(t.split(), [
            'hello', 'world'
        ])

        with self.assertRaises(TypeError):
            t.split(2)

    if __name__ == '__main__':
        unittest.main()
