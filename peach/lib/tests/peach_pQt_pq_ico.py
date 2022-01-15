import unittest
from peach.pQt import img
from peach import pDir


class TestPQt(unittest.TestCase):
    def test_pq_ico_get_icon(self):
        print(pDir.exists(pq_ico._ico_tank.get("peach").getPath("x25")))
        pxm = pq_ico.getIcon("peach", "x25")
        print(type(pxm))
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
