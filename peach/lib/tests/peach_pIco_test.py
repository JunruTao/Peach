import unittest
from peach import pIco


im = pIco.IconTank()


class IcoInitTest(unittest.TestCase):
    def test_Im_getNames(self):
        self.assertEqual(True, len(im.getNames()) > 0)  # add assertion here
        im.printNames()

    def test_Im_getTypes(self):
        self.assertEqual(True, len(im.getTypes()) > 0)  # add assertion here
        im.printTypes()

    def test_icon_test(self):
        n = im.getNames()[0]
        icon = im.get(n)
        path = icon.getPath("x50")
        print(path)
        self.assertEqual(True, bool(path))  # add assertion here


if __name__ == '__main__':
    unittest.main()
