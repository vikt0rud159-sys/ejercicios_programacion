import unittest
from unittest.mock import patch, mock_open
from unit_testing_x_3 import read_lines


class TestReadLines(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="a\nb\n")
    def test_read_lines_mocked_file(self, _):
        self.assertEqual(read_lines("x.txt"), ["a\n", "b\n"])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_read_lines_file_not_found(self, _):
        self.assertRaises(FileNotFoundError, read_lines, "x.txt")


if __name__ == "__main__":
    unittest.main()