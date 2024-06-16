This folder is the Django webserver that allowisng users to resgister and login in to the survey dashboard, which can taking the available surveys and look at the survey they have been taken.

The webserver accessing is in the code folder README.md, this one is focus on how to using the auto testing to test the webserver.

Before the terminal and enviroment we need to set the testing browser:

https://googlechromelabs.github.io/chrome-for-testing/
download chrome and chromedriver from the above link for your OS
If the C:\ driver is not a good place for your computer you could extract the folder to other place.
And then change the two line of code in the same folder called "tests_selenium.py" in line 16 and line 17.

chrome_options.binary_location = r"C:\chrome-win64\chrome.exe"  # path of Chrome binary you downloaded and extracted
chrome_service = ChromeService(executable_path=r"C:\chromedriver-win64\chromedriver.exe")  # path of your ChromeDriver you downloaded and extracted

1) create a python virtual environment

`python -m venv env`

2) ACtivate the python virtual environemnt

Windows
`.\env\Scripts\activate`

3) Install dependencies list

`pip install -r requirements.txt`

4) Run django testing

`python manage.py test surveys.tests`
`python manage.py test surveys.tests_selenium`
