'''

CS5001
Final Project
Spring 2023
MyName: Zhixiao Wang

This is a file to create a TestProcessData class and process data so that it becomes another kind of data that can be used later
'''

import unittest

from read_data_into_objects import *
from filter_data import *

# used to test the results of reading data into objects
from class_of_artist import Artist
from class_of_art import ArtWork


TWO = 2

class TestProcessData(unittest.TestCase):
    '''
    class TestProcessData: test functions that process data, including reading data into objects and filtering data
                           The aim of processing data is to make the original data become another kind of data that can be used later                
    '''
    
    def test_read_data_into_objects_by_country_with_correct_result(self):
        df1 = pd.DataFrame({"artist id": ["123", "322"], "work title": ["Sunset", "Style"], "type": ["Painting", "Mural"], "status": ["In palce", "In place"], "material": ["Unknown", "Unknown"], "neighbourhood": ["Downtown", "West End"], "year": ["2000", "2020"]})
        df2 = pd.DataFrame({"artist id": ["123", "322"], "first name": ["Unknown", "Unknown"], "last name": ["Unknown", "Unknown"], "country": ["Canada", "Canada"]})
        lst1, lst2 = read_data_into_objects_by_country(df1, df2, "Canada")
        self.assertEqual(lst1, [Artist("123", "Unknown", "Unknown", "Canada"), Artist("322", "Unknown", "Unknown", "Canada")])
        self.assertEqual(lst2, [ArtWork("Sunset", "123", "Painting", "In place", "Unknown", "Downtown", "2000"), ArtWork("Style", "322", "Mural", "In place", "Unknown", "West End", "2020")])

    def test_read_data_into_objects_by_country_with_wrong_df1(self):
        df1 = pd.DataFrame({"title": ["Sunset", "Style"], "type": ["Painting", "Mural"]})
        df2 = pd.DataFrame({"id": ["123", "322"], "country": ["Canada", "Canada"]})
        with self.assertRaises(TypeError) as te:
            read_data_into_objects_by_country("test str", df2, "year")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in read_data_into_objects_by_country(): test str should be a data frame")

    def test_read_data_into_objects_by_country_with_wrong_df2(self):
        df1 = pd.DataFrame({"title": ["Sunset", "Style"], "type": ["Painting", "Mural"]})
        df2 = pd.DataFrame({"id": ["123", "322"], "country": ["Canada", "Canada"]})
        with self.assertRaises(TypeError) as te:
            read_data_into_objects_by_country(df1, 4, "year")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in read_data_into_objects_by_country(): 4 should be a data frame")

    def test_read_data_into_objects_by_country_with_wrong_chosen_country(self):
        df1 = pd.DataFrame({"title": ["Sunset", "Style"], "type": ["Painting", "Mural"]})
        df2 = pd.DataFrame({"id": ["123", "322"], "country": ["Canada", "Canada"]})
        with self.assertRaises(TypeError) as te:
            read_data_into_objects_by_country(df1, df2, 5)
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in read_data_into_objects_by_country(): 5 should be a string")

    def test_classify_artworks_by_criterion_with_correct_result(self):
        artwork1 = ArtWork("Tears", "324", "Mural", "In place", "Unknown", "West End", "2008")
        artwork2 = ArtWork("Sunset", "112", "Painting", "In place", "Unknown", "Downtown", "2008")
        result = classify_artworks_by_criterion([artwork1, artwork2], "neighbourhood")
        self.assertEqual(result, {"West End": 1, "Downtown": 1})

    def test_classify_artworks_by_criterion_with_wrong_artworks(self):
        with self.assertRaises(TypeError) as te:
            classify_artworks_by_criterion("test", "year")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in classify_artworks_by_criterion(): test should be a list")

    def test_classify_artworks_by_criterion_with_wrong_criterion(self):
        with self.assertRaises(TypeError) as te:
            classify_artworks_by_criterion(["object1", "object2"], 5)
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "in classify_artworks_by_criterion(): 5 should be a string")

    def test_filter_artworks_by_attribute_value_with_correct_result(self):
        artwork1 = ArtWork("Tears", "324", "Mural", "In place", "Unknown", "West End", "2008")
        artwork2 = ArtWork("Sunset", "112", "Painting", "In place", "Unknown", "Downtown", "2008")
        artwork3 = ArtWork("Clouds", "112", "Site-integrated work", "In place", "Unknown", "Downtown", "2008")
        result = filter_artworks_by_attribute_value([artwork1, artwork2, artwork3], "neighbourhood", "Downtown")
        expected = [artwork2, artwork3]
        self.assertEqual(result, expected)

    def test_filter_artworks_by_attribute_value_with_wrong_artworks(self):
        with self.assertRaises(TypeError) as te:
            filter_artworks_by_attribute_value("string", "year", "2022")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "string should be a list")

    def test_filter_artworks_by_attribute_value_with_wrong_attribute(self):
        with self.assertRaises(TypeError) as te:
            filter_artworks_by_attribute_value(["artwork"], 3, "2022")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "3 should be a str")

    def test_filter_artworks_by_attribute_value_with_no_attribute(self):
        with self.assertRaises(AttributeError) as te:
            filter_artworks_by_attribute_value(["artwork"], "", "2022")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "artwork's attribute cannot be empty")

    def test_filter_artworks_by_attribute_value_with_wrong_value(self):
        with self.assertRaises(TypeError) as te:
            filter_artworks_by_attribute_value(["artwork"], "year", 2022)
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "2022 should be a str")



def main():
    
    unittest.main(verbosity = TWO)

if __name__ == "__main__":
    main()


