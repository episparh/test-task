import unittest

import HtmlTestRunner

from face_detect import face_detect


class TestStringMethods(unittest.TestCase):

    def test_group_return_number(self):
        self.assertEqual(face_detect("test_data/abba.png"), 4)

    def test_flipped_return_number(self):
        self.assertEqual(face_detect("test_data/abba_flipped.png"), 4)

    def test_sideways_return_number(self):
        self.assertEqual(face_detect("test_data/abba_sideways.png"), 4)

    def test_toon_return_zero(self):
        self.assertEqual(face_detect("test_data/toon-face.jpg"), 0)

    def test_animal_return_zero(self):
        self.assertEqual(face_detect("test_data/dog.jpg"), 0)

    def test_no_face_return_zero(self):
        self.assertEqual(face_detect("test_data/landscape.png"), 0)

    def test_text_raises_exception(self):
        self.assertRaises(Exception, face_detect, "test_data/text.txt")

    def test_no_path_to_file_raises_exception(self):
        self.assertRaises(Exception, face_detect, "test_data/")

    def test_none_raises_exception(self):
        self.assertRaises(Exception, face_detect, None)

    def test_empty_image_raises_exception(self):
        self.assertRaises(Exception, face_detect, "test_data/empty.png")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='html_report'))
