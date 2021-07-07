from selenium.webdriver.common.by import By
from base_page import BasePage


class LandingPage(BasePage):
    button_create_new = (By.CSS_SELECTOR, "[href='/Students/Create']")
    input_search = (By.ID, "Search_Data")
    btn_find = (By.CSS_SELECTOR, "input[value='Find']")
    table_data = (By.CSS_SELECTOR, "table tr:not(:first-of-type)")

    def open_create_form(self):
        self.driver.find_element(*LandingPage.button_create_new).click()

    def search(self, query):
        self.driver.find_element(*LandingPage.input_search).send_keys(query)
        self.driver.find_element(*LandingPage.btn_find).click()

    def get_first_student(self):
        row = self.driver.find_elements(*LandingPage.table_data)[0].find_elements(
            By.CSS_SELECTOR, "td:not(:last-of-type)")
        return list(map(lambda x: x.text, row))

    def edit_first_user(self):
        self.driver.find_elements(*LandingPage.table_data)[0].find_elements(
            By.CSS_SELECTOR, "td:last-of-type button")[0].click()

    def delete_first_user(self):
        self.driver.find_elements(*LandingPage.table_data)[0].find_elements(
            By.CSS_SELECTOR, "td:last-of-type button")[2].click()
