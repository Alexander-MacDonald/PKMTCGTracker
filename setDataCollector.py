from selenium import webdriver
from selenium.webdriver.common.by import By
import time

base_urls = ("https://jp.pokellector.com/sets", "https://www.pokellector.com/sets")
finalSets = []

driverOptions = webdriver.ChromeOptions()
driverOptions.add_argument("--disable-extensions")
driverOptions.add_argument("--disable-gpu")
driverOptions.add_argument("--headless")
driverOptions.add_experimental_option(
    "prefs", {
        "profile.managed_default_content_settings.images": 2 
    }
)

for url in base_urls:
    driver = webdriver.Chrome(options=driverOptions)
    driver.get(url)
    time.sleep(1)
    allSets = driver.find_element(By.ID, "columnLeft")
    subsets = allSets.find_elements(By.TAG_NAME, "div")
    for sets in subsets:
        for set in sets.find_elements(By.TAG_NAME, "a"):
            finalSets.append(set.get_attribute('href'))
    time.sleep(1)
    driver.quit()

open("sets.csv", "w", encoding="utf-8").write("\n".join(finalSets))