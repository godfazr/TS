from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains as actions

class PollPage:

# Poll url
    @property
    def url(self):
        return 'https://stage1-vote.pollstream.com/8610'
# Page load    
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
# Finilizing
    def teardown(self):
        self.driver.quit()

# Get poll question elements
    def get_elements_list(self, locator):
        self.driver.implicitly_wait(10)
        elements = self.driver.find_elements(*locator)
        return elements

# Click Submit/Continue button
    def submit_continue_click(self, locator):
        try:
            submit = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        except TimeoutError:
            print("Page not loaded yet!")
        else: 
            submit.click()

# Select answer for radio type question
    def select_radio_group_option(self, locator, option):
        radio = self.get_elements_list(locator)
        radio[option - 1].click()

# Select answer for dropdown type question
    def select_dropdown_option(self, locator, option_index):
        dd_question = Select(self.driver.find_element(*locator))
        dd_question.select_by_index(option_index)

# Select answer for checkbox type question
    def select_checkbox_options(self, locator, option_indexes):
        cb_questions = self.get_elements_list(locator)
        for i in option_indexes:
            cb_questions[i - 1].click()

# Select answer for dropdown rating type question
    def select_dropdown_rating_options(self, group_locator, option_indexes):
        dd_ratings_group = self.get_elements_list(group_locator)
        for i in range(len(option_indexes)):
            dd_rating = Select(dd_ratings_group[i])
            dd_rating.select_by_index(option_indexes[i])

# Fill input field
    def enter_answer_to_text_field(self, locator, text):
        text_field = self.driver.find_element(*locator)
        text_field.send_keys(text)

# Drag and drop rating
    def set_rating_options_by_drag_and_drop(self, source_locator, target_locator):
        self.driver.implicitly_wait(20)
        source_to_drag = self.driver.find_element(*source_locator)
        target_to_drag = self.driver.find_element(*target_locator)
        actions(self.driver).drag_and_drop(source_to_drag, target_to_drag).perform()

# Validate acknowledgement
    def verify_acknowledgement_message(self, locator, text):
        self.driver.implicitly_wait(10)
        message = self.driver.find_element(*locator).text
        try: 
            assert message == text
        except AssertionError:
            print("Something went wrong")
        else:
            print("OK")