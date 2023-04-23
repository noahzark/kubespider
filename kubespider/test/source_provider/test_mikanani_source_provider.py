import unittest
import logging
import re

from source_provider.mikanani_source_provider.provider import MikananiSourceProvider

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s: %(message)s')
class MikkananiSouirceProviderTest(unittest.TestCase):
    def setUp(self) -> None:
        self.provider = MikananiSourceProvider("test")
        # 一共7个记录
        self.test_file = "./test/source_provider/test_source.txt"

    def load(self, reg) -> dict:
        if reg is not None:
            pattern = re.compile(reg)
        else:
            pattern = None
        with open(self.test_file, encoding="utf-8", mode= 'r') as test_file:
            lines = test_file.readlines()
        return list(filter(lambda p: p is not None, map(lambda p: self.provider.check_anime_title(p, pattern), lines)))

    def test_title_filter_full(self):
        title_dict = self.load(None)
        self.assertEqual(7, len(title_dict))

    def test_title_filter_reg_include(self):
        title_dict = self.load( ".*简.*")
        self.assertEqual(3, len(title_dict))

    def test_title_filter_reg_except(self):
        title_dict = self.load( "^((?!繁).)*$")
        self.assertEqual(4, len(title_dict))
