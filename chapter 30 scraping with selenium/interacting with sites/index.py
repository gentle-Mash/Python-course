from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= options)

driver.get("https://www.python.org/")

search = driver.find_element(By.NAME, "q")
search.send_keys("selenium")

go = driver.find_element(By.ID, "submit")
go.click()