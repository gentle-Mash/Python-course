
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= options)

driver.get("https://www.python.org/")

logo = driver.find_element(By.CLASS_NAME, "python-logo")

search_bar = driver.find_element(By.NAME, "q")

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")

submit_event = driver.find_element(By.XPATH, '//*[@id="container"]/li[7]/ul/li[5]/a')

print(logo.get_attribute("alt"), search_bar.get_attribute("placeholder"))
print(documentation_link.get_attribute("href"), submit_event.text)




