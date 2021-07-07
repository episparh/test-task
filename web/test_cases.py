import unittest
from datetime import date

from selenium import webdriver

from landing_page import LandingPage
from student_form import StudentForm


class TestCases(unittest.TestCase):
    home, driver = None, None
    test_first_name, test_last_name, today = "Tes21312312321312312", "User", str(date.today())

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://uitestpractice.com/Students/Index")
        self.home = LandingPage(driver=self.driver)
        self.student_form = StudentForm(driver=self.driver)

    def test_create_student(self):
        self.home.open_create_form()
        self.student_form.create(self.test_first_name, self.test_last_name, self.today)
        self.assertEqual(self.driver.current_url, "http://uitestpractice.com/Students/Index")
        # the following is anti pattern. I would rather prefer verification in DB or through api calls
        self.home.search(self.test_first_name)
        self.assertEqual(self.home.get_first_student(), [self.test_first_name, self.test_last_name, self.today])

    def test_search_and_read(self):
        self.home.search(self.test_first_name)
        self.assertEqual(self.home.get_first_student(), [self.test_first_name, self.test_last_name, self.today])
        self.assertEqual(self.driver.current_url, "http://uitestpractice.com/Students/Index")

    def test_edit(self):
        self.home.search(self.test_first_name)
        self.home.edit_first_user()
        self.student_form.edit(self.test_first_name + "(Edited)", self.test_last_name + "(Edited)", self.today)
        self.assertEqual(self.driver.current_url, "http://uitestpractice.com/Students/Index")
        # the following is anti pattern. I would rather prefer verification in DB or through api calls
        self.home.search(self.test_first_name)
        self.assertEqual(self.home.get_first_student(),
                         [self.test_first_name + "(Edited)", self.test_last_name + "(Edited)", self.today])

    def test_delete(self):
        self.home.search(self.test_first_name + "(Edited)")
        self.home.delete_first_user()
        self.student_form.delete()
        self.assertEqual(self.driver.current_url, "http://uitestpractice.com/Students/Index")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.main()
