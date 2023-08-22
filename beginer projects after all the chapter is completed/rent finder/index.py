import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= options)

driver.get("https://www.zillow.com/manchester-ct/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Manchester%20CT%22%2C%22mapBounds%22%3A%7B%22west%22%3A-72.62932440820313%2C%22east%22%3A-72.41783759179688%2C%22south%22%3A41.71509032427475%2C%22north%22%3A41.8390090307334%7D%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A398963%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A558233%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D")

driver.maximize_window()

for i in range(6,44):
    searched_item = driver.find_element(By.XPATH, f'//*[@id="grid-search-results"]/ul/li[{i}]')
    if i == 17:
        continue
    driver.execute_script("arguments[0].scrollIntoView();", searched_item)
    
address_tags = driver.find_elements(By.CSS_SELECTOR, ".ListItem-c11n-8-84-3__sc-10e22w8-0 address") 
address_text = [n.text for n in address_tags]

all_links = driver.find_elements(By.CSS_SELECTOR, ".ListItem-c11n-8-84-3__sc-10e22w8-0 a")
link_text = [l.get_attribute("href") for l in all_links]

all_price_tags = driver.find_elements(By.CSS_SELECTOR, ".iMKTKr")
all_prices = [price.text.split("$")[-1] for price in all_price_tags]

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfaBfwkYlU4MPQ4tD2sentsz-PkTYiDxrS1_fJ0l1-SJGxezQ/viewform")
time.sleep(2)

for i in range(0,len(address_text)):

    time.sleep(1.5)

    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.click()
    address.send_keys(address_text[i])

    price.click()
    price.send_keys(all_prices[i])

    link.click()
    link.send_keys(link_text[i])

    time.sleep(1.5)
    submit_button.click()
    time.sleep(1.5)
    
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

