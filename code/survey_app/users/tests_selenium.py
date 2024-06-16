from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from surveys.models import Survey, Question

class SurveySeleniumTests(StaticLiveServerTestCase):

    def setUp(self):
        chrome_options = Options()
        #https://googlechromelabs.github.io/chrome-for-testing/
        #download chrome and chromedriver from the above link for your OS
        chrome_options.binary_location = r"C:\chrome-win64\chrome.exe"  # path of Chrome binary you downloaded and extracted
        chrome_service = ChromeService(executable_path=r"C:\chromedriver-win64\chromedriver.exe")  # path of your ChromeDriver you downloaded and extracted

        self.browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.survey = Survey.objects.create(title='Test Survey', description='Test Survey Description')
        self.question1 = Question.objects.create(survey=self.survey, text='Question 1')
        self.question2 = Question.objects.create(survey=self.survey, text='Question 2')

    def tearDown(self):
        self.browser.quit()

    def test_register_login_take_and_view_survey(self):
        # Register a new user
        self.browser.get(self.live_server_url + reverse('register'))
        
        email_input = self.browser.find_element(By.NAME, "email")
        first_name_input = self.browser.find_element(By.NAME, "first_name")
        last_name_input = self.browser.find_element(By.NAME, "last_name")
        password1_input = self.browser.find_element(By.NAME, "password1")
        password2_input = self.browser.find_element(By.NAME, "password2")
        
        email_input.send_keys('testuser@example.com')
        first_name_input.send_keys('Test')
        last_name_input.send_keys('User')
        password1_input.send_keys('Testtest123!')
        password2_input.send_keys('Testtest123!')
        password2_input.send_keys(Keys.RETURN)
        
        # Login with the newly registered user
        self.browser.get(self.live_server_url + reverse('login'))
        
        email_input = self.browser.find_element(By.NAME, "email")
        password_input = self.browser.find_element(By.NAME, "password")
        email_input.send_keys('testuser@example.com')
        password_input.send_keys('Testtest123!')
        password_input.send_keys(Keys.RETURN)

        # Navigate to take survey
        self.browser.get(self.live_server_url + reverse('take_survey', args=[self.survey.id]))

        # Submit survey
        form_elements = self.browser.find_elements(By.CSS_SELECTOR, 'input[type="radio"]')
        for element in form_elements:
            element.click()
        submit_button = self.browser.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()

        # Check if redirected to dashboard
        self.assertIn('Dashboard', self.browser.page_source)

        # View taken survey
        taken_survey_link = self.browser.find_element(By.LINK_TEXT, self.survey.title)
        taken_survey_link.click()
        self.assertIn('Question 1', self.browser.page_source)
        self.assertIn('Question 2', self.browser.page_source)
        