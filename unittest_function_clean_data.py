'''
CS5001
Final Project
Spring 2023
MyName: Zhixiao Wang

This is a file to create a TestCleanData class and test functions that clean data
'''


import unittest

from get_and_clean_art_data import replace_art_empty_with_unknown
from get_and_clean_artist_data import replace_artist_empty_with_unknown

TWO = 2

class TestCleanData(unittest.TestCase):
    '''
    class TestCleanData: test functions that clean up data by replacing the empty string with Unknown                 
    '''

    def test_replace_art_empty_with_unknown_with_correct_result(self):
        result = replace_art_empty_with_unknown(["Sunset", "421", "Painting", "", "", "Downtown", ""])
        self.assertEqual(result, ["Sunset", "421", "Painting", "Unknown", "Unknown", "Downtown", "Unknown"])

    def test_replace_art_empty_with_unknown_with_wrong_type(self):
        with self.assertRaises(TypeError) as te:
            replace_art_empty_with_unknown("string")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "In replace_art_empty_with_unknown(), string should be a list")

    def test_replace_artist_empty_with_unknown_with_correct_result(self):
        result = replace_artist_empty_with_unknown(["612", "", "Anna", "Canada"])
        self.assertEqual(result, ["612", "Unknown", "Anna", "Canada"])

    def test_replace_artist_empty_with_unknown_with_wrong_input(self):
        with self.assertRaises(TypeError) as te:
            replace_artist_empty_with_unknown(123)
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "In replace_artist_empty_with_unknown(), 123 should be a list")


def main():
    
    unittest.main(verbosity = TWO)

if __name__ == "__main__":
    main()
