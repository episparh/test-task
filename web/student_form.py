from selenium.webdriver.common.by import By

from base_page import BasePage


class StudentForm(BasePage):
    first_name = (By.ID, "FirstName")
    last_name = (By.ID, "LastName")
    enrollment_date = (By.ID, "EnrollmentDate")
    btn_submit = (By.CSS_SELECTOR, "input[value='Create'] , input[value='Save'], input[value='Delete']")

    def create(self, first_name, last_name, enrollment_date):
        self.driver.find_element(*StudentForm.first_name).send_keys(first_name)
        self.driver.find_element(*StudentForm.last_name).send_keys(last_name)
        self.driver.find_element(*StudentForm.enrollment_date).send_keys(enrollment_date)
        self.driver.find_element(*StudentForm.btn_submit).click()

    def edit(self, first_name, last_name, enrollment_date):
        first_name_element = self.driver.find_element(*StudentForm.first_name)
        first_name_element.clear()
        first_name_element.send_keys(first_name)
        last_name_element = self.driver.find_element(*StudentForm.last_name)
        last_name_element.clear()
        last_name_element.send_keys(last_name)
        enrolment_date_element = self.driver.find_element(*StudentForm.enrollment_date)
        enrolment_date_element.clear()
        enrolment_date_element.send_keys(enrollment_date)
        self.driver.find_element(*StudentForm.btn_submit).click()

    def delete(self):
        self.driver.find_element(*StudentForm.btn_submit).click()
