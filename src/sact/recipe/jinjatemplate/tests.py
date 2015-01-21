import os
import unittest


class TestRecipe(unittest.TestCase):

    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    result_dir = os.path.abspath(os.path.join(CURRENT_DIR, "templates"))

    def test_simple(self):
        file_1_path = os.path.join(self.result_dir, "test1.result")
        file_2_path = os.path.join(self.result_dir, "test2.result")

        file_1 = open(file_1_path).read()
        file_2 = open(file_2_path).read()

        self.assertEquals(file_1, file_2)

    def test_shell(self):
        file_shell_path = os.path.join(self.result_dir, "test_shell.result")
        file_shell = open(file_shell_path).read()

        result_without_quote = "; rm -rf /*"
        result_with_quote = "'; rm -rf /*'"

        lines = file_shell.split('\n')
        self.assertEquals(lines[0], result_without_quote)
        self.assertEquals(lines[1], result_with_quote)

    def test_split(self):
        file1_path = os.path.join(self.result_dir, "test_split.result")
        file1 = open(file1_path).read()
        result = "a\nb\nc\nd\n"
        self.assertEquals(result, file1)
