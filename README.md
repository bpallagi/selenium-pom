selenium-pom

Please install these:

chromedriver
Open: https://chromedriver.chromium.org/downloads
Check Chrome version and !DONT FORGET! to check your architecture
download the correct driver
unzip next to Src\TestBase
Edit file Src\TestBase\WebDriverSetup.py
put the correct filename in the arg field. 
self.driver = webdriver.Chrome(r'Src\TestBase\chromedriver.exe')


install python 3.8+
pip install selenium
pip install chromedriver

check permissions to run python programs
