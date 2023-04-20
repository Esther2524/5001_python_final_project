'''
CS5001
Final Project
Spring 2023
MyName: Zhixiao Wang

This is a file to create a ArtWorkTest class to test ArtWork class.
'''

import unittest

from class_of_art import ArtWork

TWO = 2

class ArtWorkTest(unittest.TestCase):
    '''
    class ArtWorkTest: test class ArtWork's __init__,  __str__, __hash__ and __eq__.                      
    '''
    def test_init_basic_with_int(self):
        artwork1 = ArtWork("Angel of Victory", "94", "Memorial or monument", "In place", "bronze", "Downtown", "1921")
        self.assertEqual(artwork1.title, "Angel of Victory")
        self.assertEqual(artwork1.id, "94")
        self.assertEqual(artwork1.type, "Memorial or monument")
        self.assertEqual(artwork1.status, "In place")
        self.assertEqual(artwork1.material, "bronze")
        self.assertEqual(artwork1.neighbourhood, "Downtown")
        self.assertEqual(artwork1.year, "1921")

        artwork2 = ArtWork("Street Light", "147,177", "Sculpture", "In place", "Bronze, glass", "Downtown", "1997")
        self.assertEqual(artwork2.title, "Street Light")
        self.assertEqual(artwork2.id, "147,177")
        self.assertEqual(artwork2.type, "Sculpture")
        self.assertEqual(artwork2.status, "In place")
        self.assertEqual(artwork2.material, "Bronze, glass")
        self.assertEqual(artwork2.neighbourhood, "Downtown")
        self.assertEqual(artwork2.year, "1997")

    def test_init_title_with_wrong_int(self):
        with self.assertRaises(TypeError) as te:
            ArtWork(324, "107", "Fountain or water feature", "In place", "Stone mosaic", "Downtown", "1995")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The title '324' should be a string")

    def test_init_title_with_wrong_float(self):
        with self.assertRaises(TypeError) as te:
            ArtWork(32.4, "107", "Fountain or water feature", "In place", "Stone mosaic", "Downtown", "1995")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The title '32.4' should be a string")

    def test_init_id_with_wrong_int(self):
        with self.assertRaises(TypeError) as te:
            ArtWork("Fountain of Time", 107, "Fountain or water feature", "In place", "Stone mosaic", "Downtown", "1995")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The id '107' should be a string")

    def test_init_id_with_wrong_float(self):
        with self.assertRaises(TypeError) as te:
            ArtWork("Fountain of Time", -10.7, "Fountain or water feature", "In place", "Stone mosaic", "Downtown", "1995")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The id '-10.7' should be a string")
    
    def test_init_type_with_wrong_int(self):
        with self.assertRaises(TypeError) as te:
            ArtWork("Fountain of Time", "107", 3, "In place", "Stone mosaic", "Downtown", "1995")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The type '3' should be a string")

    def test_init_type_with_wrong_float(self):
        with self.assertRaises(TypeError) as te:
            ArtWork("Fountain of Time", "107", 3.3, "In place", "Stone mosaic", "Downtown", "1995")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The type '3.3' should be a string")

    def test_init_status_with_wrong_int(self):
        with self.assertRaises(TypeError) as te:
            ArtWork("Fountain of Time", "107", "Fountain or water feature", 6, "Stone mosaic", "Downtown", "1995")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The status '6' should be a string")

    def test_init_status_with_wrong_float(self):
        with self.assertRaises(TypeError) as te:
            ArtWork("Fountain of Time", "107", "Fountain or water feature", -6.2, "Stone mosaic", "Downtown", "1995")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The status '-6.2' should be a string")

    def test_init_material_with_wrong_int(self):
        with self.assertRaises(TypeError) as te:
            ArtWork("Fountain of Time", "107", "Fountain or water feature", "In place", 32, "Downtown", "1995")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The material '32' should be a string")

    def test_init_material_with_wrong_float(self):
        with self.assertRaises(TypeError) as te:
            ArtWork("Fountain of Time", "107", "Fountain or water feature", "In place", -3.2, "Downtown", "1995")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The material '-3.2' should be a string")

    def test_init_neighbourhood_with_wrong_int(self):
        with self.assertRaises(TypeError) as te:
            ArtWork("Fountain of Time", "107", "Fountain or water feature", "In place", "Stone mosaic", 101, "1995")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The neighbourhood '101' should be a string")

    def test_init_neighbourhood_with_wrong_int(self):
        with self.assertRaises(TypeError) as te:
            ArtWork("Fountain of Time", "107", "Fountain or water feature", "In place", "Stone mosaic", 1.01, "1995")
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The neighbourhood '1.01' should be a string")

    def test_init_year_with_wrong_int(self):
        with self.assertRaises(TypeError) as te:
            ArtWork("Fountain of Time", "107", "Fountain or water feature", "In place", "Stone mosaic", "Downtown", 1995)
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The year '1995' should be a string")

    def test_init_year_with_wrong_int(self):
        with self.assertRaises(TypeError) as te:
            ArtWork("Fountain of Time", "107", "Fountain or water feature", "In place", "Stone mosaic", "Downtown", 19.95)
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The year '19.95' should be a string")

    def test_str(self):
        artwork3 = ArtWork("Fountain of Time", "107", "Fountain or water feature", "In place", "Stone mosaic", "Downtown", "1995")
        self.assertEqual(artwork3.__str__(), "Fountain of Time (from artist id 107)")

    def test_eq_with_same_class_and_equal(self):
        artwork4 = ArtWork("Street Light", "147", "Sculpture", "In place", "Bronze, glass", "Downtown", "1997")
        artwork5 = ArtWork("Street Light", "144", "Sculpture", "In place", "Bronze, glass", "Downtown", "1997")
        self.assertTrue(artwork4 == artwork5)

    def test_eq_with_same_title_and_equal(self):
        artwork6 = ArtWork("Street Light", "147", "Sculpture", "In place", "Bronze, glass", "Downtown", "1997")
        artwork7 = ArtWork("Street Light", "144", "Unknown", "Unknown", "Unknown", "Unknown", "Unknown")
        self.assertTrue(artwork6 == artwork7)

    def test_eq_with_same_class_but_not_equal(self):
        artwork8 = ArtWork("Street Light", "147", "Sculpture", "In place", "Bronze, glass", "Downtown", "1997")
        artwork9 = ArtWork("Semaphores", "178", "Site-integrated work", "In place", "Bronze, glass", "Downtown", "2003")
        self.assertFalse(artwork8 == artwork9)

    def test_eq_with_same_info_but_not_equal(self):
        artwork10 = ArtWork("Street Light", "147", "Sculpture", "In place", "Bronze, glass", "Downtown", "1997")
        artwork11 = ArtWork("Street", "147", "Sculpture", "In place", "Bronze, glass", "Downtown", "1997")
        self.assertFalse(artwork10 == artwork11)

    def test_eq_with_worng_str(self):
        with self.assertRaises(TypeError) as te:
            artwork10 = ArtWork("Street Light", "147", "Sculpture", "In place", "Bronze, glass", "Downtown", "1997")
            artwork10 == "Street Light"
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The compared 'Street Light' should be an ArtWork instance")
    
    def test_eq_with_worng_float(self):
        with self.assertRaises(TypeError) as te:
            artwork10 = ArtWork("Street Light", "147", "Sculpture", "In place", "Bronze, glass", "Downtown", "1997")
            artwork10 == 14.7
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The compared '14.7' should be an ArtWork instance")

    def test_eq_with_worng_int(self):
        with self.assertRaises(TypeError) as te:
            artwork10 = ArtWork("Street Light", "147", "Sculpture", "In place", "Bronze, glass", "Downtown", "1997")
            artwork10 == 147
        exception_message = str(te.exception)
        self.assertEqual(exception_message, "The compared '147' should be an ArtWork instance")

    def test_hash_and_equal(self):
        artwork12 = ArtWork("Walls of Change", "178", "Mural", "No longer in place", "Latex paint, spraypaint", "DowntownEastside", "1998")
        artwork13 = ArtWork("Walls of Change", "218", "Mural", "No longer in place", "Latex paint, spraypaint", "DowntownEastside", "1998")
        self.assertEqual(hash(artwork12), hash(artwork13))

    def test_hash_and_not_equal(self):
        artwork12 = ArtWork("Walls of Change", "178", "Mural", "No longer in place", "Latex paint, spraypaint", "DowntownEastside", "1998")
        artwork14 = ArtWork("Street Light", "147", "Sculpture", "In place", "Bronze, glass", "Downtown", "1997")
        self.assertNotEqual(hash(artwork12), hash(artwork14))



def main():

    unittest.main(verbosity = TWO)

if __name__ == "__main__":
    main()