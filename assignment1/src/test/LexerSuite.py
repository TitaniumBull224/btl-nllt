import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(
            TestLexer.test(
                """var.12349""",
                "this,<EOF>",
                101,
            )
        )
