import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options= options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

wait = WebDriverWait(driver, 10)

go = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/a[1]")))
go.click()

language = wait.until(EC.presence_of_element_located((By.ID, "langSelect-EN")))
language.click()


time.sleep(4)
big_cookie = driver.find_element(By.ID, "bigCookie")

five_min = time.time() + 5*60
time_out = time.time() + 8

while True:
    big_cookie.click()
    
    if time.time() >= time_out:
        try:
            my_cookies = int(driver.find_element(By.ID, "cookies").text.split()[0])
        except ValueError:
            cookies = driver.find_element(By.ID, "cookies").text.split()[0].split(",")
            my_cookies = int("".join(cookies))

        upgrades = driver.find_elements(By.CLASS_NAME, "unlocked")
        upgrade_prices_element = driver.find_elements(By.CSS_SELECTOR, ".unlocked.enabled .price")
        upgrade_prices = []
        for price in upgrade_prices_element:
            try:
                upgrade_prices.append(int(price.text))
            except ValueError:
                big_price = price.text.split(",")
                big_price_str = "".join(big_price)
                upgrade_prices.append(int(big_price_str))

        max_price = max(upgrade_prices)
        index = upgrade_prices.index(max_price)

        while my_cookies > max_price:
            upgrades[index].click()
            try:
                my_cookies = int(driver.find_element(By.ID, "cookies").text.split()[0])
            except ValueError:
                cookies = driver.find_element(By.ID, "cookies").text.split()[0].split(",")
                my_cookies = int("".join(cookies))
            upgrade_prices_element = driver.find_elements(By.CSS_SELECTOR, ".unlocked .price")
            upgrade_prices = []
            for price in upgrade_prices_element:
                try:
                    upgrade_prices.append(int(price.text))
                except ValueError:
                    big_price = price.text.split(",")
                    big_price_str = "".join(big_price)
                    upgrade_prices.append(int(big_price_str))

            max_price = max(upgrade_prices)
            index = upgrade_prices.index(max_price)
                
            time_out = time.time() + 8

        if time.time() > five_min:
            cookie_per_s = driver.find_element(By.ID, "cookiesPerSecond")
            print(cookie_per_s.text)
            break

            

            
            

