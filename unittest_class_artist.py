'''
CS5001
Final Project
Spring 2023
MyName: Zhixiao Wang

This is a file to create a ArtistTest class and test Artist class.
'''


import unittest

from class_of_artist import Artist

TWO = 2

class TestArtist(unittest.TestCase):
    '''
    class ArtistTest: test class Artist's __init__,  __str__, and __eq__.                      
    '''
    def test_init_basic_with_int(self):
        artist1 = Artist("336", "Aaron", "Nelson-Moody", "Canada")
        self.assertEqual(artist1.id, "336")
        self.assertEqual(artist1.first_name, "Aaron")
        self.assertEqual(artist1.last_name, "Nelson-Moody")
        self.assertEqual(artist1.country, "Canada")

        artist2 = Artist("215", "Lawrence", "Weiner", "USA")
        self.assertEqual(artist2.id, "215")
        self.assertEqual(artist2.first_name, "Lawrence")
        self.assertEqual(artist2.last_name, "Weiner")
        self.assertEqual(artist2.country, "USA")

    def test_init_id_with_wrong_int(self):
        with self.assertRaises(TypeError) as te:
            Artist(60, "Don", "Yeomans", "Canada")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The id '60' should be a string")

    def test_init_id_with_wrong_float(self):
        with self.assertRaises(TypeError) as te:
            Artist(6.0, "Don", "Yeomans", "Canada")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The id '6.0' should be a string")

    def test_init_first_name_with_wrong_int(self):
        with self.assertRaises(TypeError) as te:
            Artist("325", 12, "Creed", "Italy")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The first name '12' should be a string")

    def test_init_first_name_with_wrong_float(self):
        with self.assertRaises(TypeError) as te:
            Artist("325", -1.2, "Creed", "Italy")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The first name '-1.2' should be a string")

    def test_init_last_name_with_wrong_int(self):
        with self.assertRaises(TypeError) as te:
            Artist("171", "Wolfgang", -44, "Germany")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The last name '-44' should be a string")

    def test_init_last_name_with_wrong_float(self):
        with self.assertRaises(TypeError) as te:
            Artist("171", "Wolfgang", 4.4, "Germany")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The last name '4.4' should be a string")

    def test_init_country_with_wrong_int(self):
        with self.assertRaises(TypeError) as te:
            Artist("434", "Li", "Ming", 123)
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The country '123' should be a string")

    def test_init_country_with_wrong_int(self):
        with self.assertRaises(TypeError) as te:
            Artist("434", "Li", "Ming", -1.23)
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The country '-1.23' should be a string")

    def test_eq_with_same_class_and_equal(self):
        artist3 = Artist("434", "Li", "Ming", "China")
        self.assertTrue(artist3 == Artist("434", "Unknown", "Unknown", "Unknown"))

    def test_eq_with_same_class_and_not_equal(self):
        artist3 = Artist("434", "Li", "Ming", "China")
        self.assertFalse(artist3 == Artist("589", "Shigeru", "Ban", "Japan"))

    def test_eq_with_wrong_int(self):
        with self.assertRaises(TypeError) as te:
            Artist("141", "Jiro", "Sugawara", "Japan") == 141
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The compared '141' should be an Artist instance")
    
    def test_eq_with_wrong_str(self):
        with self.assertRaises(TypeError) as te:
            Artist("141", "Jiro", "Sugawara", "Japan") == "Jiro"
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The compared 'Jiro' should be an Artist instance")

    def test_eq_with_wrong_float(self):
        with self.assertRaises(TypeError) as te:
            Artist("141", "Jiro", "Sugawara", "Japan") == -1.3
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The compared '-1.3' should be an Artist instance")

    def test_str(self):
        artist4 = Artist("23", "Dale", "Chihuly", "USA")
        self.assertEqual(artist4.__str__(), "artist 23 from USA")


               
def main():

    unittest.main(verbosity = TWO)

if __name__ == "__main__":
    main()