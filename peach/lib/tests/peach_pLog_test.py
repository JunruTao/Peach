import unittest
from peach import pLog


class PlogTest(unittest.TestCase):
    def test_plog_printings(self):
        pLog.message("test_class: msg", cls=self, fn=pLog.message, state="MSG")
        pLog.debug("test_str: debug", cls="something", fn=pLog.debug)
        pLog.warning("test_cls: warning", cls=self, fn=self.test_plog_printings)

    def test_plog_error(self):
        try:
            import hou
        except ImportError as e:
            pLog.warning("can not import hou", cls=self, fn=pLog.warning)
            # pLog.error("can not import hou", cls=self, fn=pLog.error, e=e)
            # [ error raise passed ]


if __name__ == '__main__':
    unittest.main()
