Sample project for web and api testing

Selenium + page object modell
Python api testing withrequests package

Please install these:

chromedriver
Open: https://chromedriver.chromium.org/downloads
Check Chrome version and !DONT FORGET! to check your architecture
download the correct driver
unzip next to Src\TestBase
Edit file Src\TestBase\WebDriverSetup.py
put the correct filename in the arg field.

EXAMPLE : self.driver = webdriver.Chrome(r'Src\TestBase\chromedriver.exe')

install python 3.8+
pip install -U pytest pytest-html
pip install -U selenium
pip install -U chromedriver
pip install -U requests
pip install -U jsonschema

Reporting:

For basic usage you can use the pytest html report capability

pytest -sv --html report.html
