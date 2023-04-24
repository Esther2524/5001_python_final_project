'''

CS5001
Final Project
Spring 2023
MyName: Zhixiao Wang

This is a file to create a TestFetchData class and test functions that fetch data
'''

import unittest

from get_and_clean_art_data import *
from get_and_clean_artist_data import *

TWO = 2

class TestFetchData(unittest.TestCase):

    '''
    class TestFetchData: test functions that fetch data (from a csv file to a list of lists)              
    '''

    '''
    I already catch the HTTPError exception using the try-except block and printing a message in the function itself.
    self.assertRaises(requests.exceptions.HTTPError) didn't work since the function didn't raise the exception again

    The way to test whether the httpError has been caught is that I pass a 404 URL into it, 
    and then see if the information behind the unit test is correct
    '''
    
    def test_get_art_csv_file_with_http_error(self):
        get_art_csv_file("https://www.pipsnacks.com/404")
  
    def test_get_art_csv_file_with_wrong_input(self):
        with self.assertRaises(TypeError) as te:
            get_art_csv_file(5)
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "5 should be a str")

    def test_get_work_title_from_art_table_with_correct_result(self):
        content = "\r\n123;Sunset;Canada\r\n133;Tears;USA\r\n"
        result = get_work_title_from_art_table(content)
        self.assertEqual(result, ["Sunset", "Tears"])

    def test_get_work_title_from_art_table_with_wrong_type(self):
        with self.assertRaises(TypeError) as te:
            get_work_title_from_art_table(1233)
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in get_work_title_from_art_table(), 1233 should be a string")

    def test_get_other_info_from_art_table_with_correct_result(self):
        content = ";Painting;In place;;;;https://regex101.com;;;Downtown;"
        type, status, material, neighbourhood = get_other_info_from_art_table(content)
        self.assertEqual(type, ["Painting"])
        self.assertEqual(status, ["In place"])
        self.assertEqual(material, ["Unknown"])
        self.assertEqual(neighbourhood, ["Downtown"])

    def test_get_other_info_from_art_table_with_wrong_input(self):
        with self.assertRaises(TypeError) as te:
            get_other_info_from_art_table(5)
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "In get_other_info_from_art_table(), 5 should be a string")

    def test_get_artist_id_and_year_from_art_table_with_correct_result(self):
        content = "work_id;other;artist_id;other;year;other\r\n122;other;355, 345;other;2000;other\r\n123;other;490;other;1999;other\r"
        id, year = get_artist_id_and_year_from_art_table(content)
        self.assertEqual(id, ["355, 345", "490"])
        self.assertEqual(year, ["2000", "1999"])
       
    def test_get_artist_id_and_year_from_art_table_with_wrong_type(self):
        with self.assertRaises(TypeError) as te:
            get_artist_id_and_year_from_art_table(-34.5)
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in get_artist_id_and_year_from_art_table(), -34.5 should be a string")

    def test_get_public_art_data_with_correct_result(self):
        data_of_art_table = get_public_art_data(["Style", "Afterglow"],["Mural", "Sculpture"], ["In place", "Unknown"], ["Unknown", "Unknown"], ["Downtown", "Unknown"], ["624", "575"], ["2020", "2008"])
        self.assertEqual(data_of_art_table, [["Style", "624", "Mural", "In place", "Unknown", "Downtown", "2020"], ["Afterglow", "575", "Sculpture", "Unknown", "Unknown", "Unknown", "2008"]])
    
    def test_get_public_art_data_with_wrong_work_title(self):
        with self.assertRaises(TypeError) as te:
            get_public_art_data("Style", ["Mural"], ["In place"], ["Unknown"], ["Downtown"], ["624"], ["2020"])
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in get_public_art_data(): the Style should be a list")

    def test_get_public_art_data_with_wrong_type(self):
        with self.assertRaises(TypeError) as te:
            get_public_art_data(["Style"], "Mural", ["In place"], ["Unknown"], ["Downtown"], ["624"], ["2020"])
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in get_public_art_data(): the Mural should be a list")

    def test_get_public_art_data_with_wrong_status(self):
        with self.assertRaises(TypeError) as te:
            get_public_art_data(["Style"],["Mural"], "In place", ["Unknown"], ["Downtown"], ["624"], ["2020"])
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in get_public_art_data(): the In place should be a list")

    def test_get_public_art_data_with_wrong_material(self):
        with self.assertRaises(TypeError) as te:
            get_public_art_data(["Style"],["Mural"], ["In place"], 0, ["Downtown"], ["624"], ["2020"])
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in get_public_art_data(): the 0 should be a list")

    def test_get_public_art_data_with_wrong_neighbourhood(self):
        with self.assertRaises(TypeError) as te:
            get_public_art_data(["Style"],["Mural"], ["In place"], ["Unknown"], 4.5, ["624"], ["2020"])
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in get_public_art_data(): the 4.5 should be a list")

    def test_get_public_art_data_with_wrong_artist_id(self):
        with self.assertRaises(TypeError) as te:
            get_public_art_data(["Style"],["Mural"], ["In place"], ["Unknown"], ["Downtown"], 624, ["2020"])
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in get_public_art_data(): the 624 should be a list")

    def test_get_public_art_data_with_wrong_year(self):
        with self.assertRaises(TypeError) as te:
            get_public_art_data(["Style"],["Mural"], ["In place"], ["Unknown"], ["Downtown"], ["624"], 2020)
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in get_public_art_data(): the 2020 should be a list")

    def test_get_public_art_data_with_wrong_list_length(self):
        with self.assertRaises(ValueError) as te:
            get_public_art_data(["Style", "Afterglow"],["Mural", "Sculpture"], ["In place", "Unknown"], ["Unknown", "Unknown"], ["Downtown"], ["624", "575"], ["2020"])
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in get_public_art_data(), the length of lists should be identical")

    def test_get_artist_csv_file_with_wrong_input(self):
        with self.assertRaises(TypeError) as te:
            get_artist_csv_file(-1.2)
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "-1.2 should be a str")

    def test_get_artist_csv_file_with_http_error(self):
        get_artist_csv_file("https://www.pipsnacks.com/404")

    def test_get_basic_info_from_artist_table_with_correct_result(self):
        content = "\r\n132;Kirsty;Robbins;https://opendata.vancouver.ca123;"
        id, first_name, last_name = get_basic_info_from_artist_table(content)
        self.assertEqual(id, ["132"])
        self.assertEqual(first_name, ["Kirsty"])
        self.assertEqual(last_name, ["Robbins"])

    def test_get_basic_info_from_artist_table_with_wrong_input(self):
        with self.assertRaises(TypeError) as te:
            get_basic_info_from_artist_table(5.5)
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in get_basic_info_from_artist_table(), 5.5 should be a string")

    def test_get_country_from_artist_table_with_correct_result(self):
        content = "id;other;country;other;other;other\r\n123;other;Canada;;;\r\n122;other;USA;;;other\r"
        country = get_country_from_artist_table(content)
        self.assertEqual(country, ["Canada", "USA"])

    def test_get_country_from_artist_table_with_wrong_input(self):
        with self.assertRaises(TypeError) as te:
            get_country_from_artist_table(3)
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "get_country_from_artist_table(): 3 should be a string")

    def test_get_public_arist_data_with_correct_input(self):
        result = get_public_arist_data(["144", "244"], ["Bob", "Tony"], ["Unknown", "Bloom"], ["Canada", "Unknown"])
        self.assertEqual(result, [["144", "Bob", "Unknown", "Canada"], ["244", "Tony", "Bloom", "Unknown"]])

    def test_get_public_arist_data_with_wrong_artist_id(self):
        with self.assertRaises(TypeError) as te:
            get_public_arist_data(134, ["Don"], ["Yeomans"], ["Canada"])
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in get_public_arist_data(): the 134 should be a list")

    def test_get_public_arist_data_with_wrong_first_name(self):
        with self.assertRaises(TypeError) as te:
            get_public_arist_data(["60"], "Don", ["Yeomans"], ["Canada"])
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in get_public_arist_data(): the Don should be a list")

    def test_get_public_arist_data_with_wrong_last_name(self):
        with self.assertRaises(TypeError) as te:
            get_public_arist_data(["60"], ["Don"], 32, ["Canada"])
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in get_public_arist_data(): the 32 should be a list")

    def test_get_public_arist_data_with_wrong_last_name(self):
        with self.assertRaises(TypeError) as te:
            get_public_arist_data(["60"], ["Don"], ["Yeomans"], "Canada")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in get_public_arist_data(): the Canada should be a list")

    def test_get_public_arist_data_with_wrong_list_length(self):
        with self.assertRaises(ValueError) as te:
            get_public_arist_data(["60", "166"], ["Don"], ["Yeomans"], ["Canada"])
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in get_public_arist_data(): the length of lists should be identical")


def main():
    
    unittest.main(verbosity = TWO)

if __name__ == "__main__":
    main()


