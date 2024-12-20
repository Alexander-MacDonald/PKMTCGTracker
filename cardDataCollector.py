from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import constants

driverOptions = webdriver.ChromeOptions()
driverOptions.add_argument("--disable-extensions")
driverOptions.add_argument("--disable-gpu")
driverOptions.add_argument("--headless")
driverOptions.add_experimental_option(
    "prefs", {
        "profile.managed_default_content_settings.images": 2 
    }
)

sets = open("sets.csv", "r", encoding="utf-8").read().split("\n")

for set in sets:
    time.sleep(1)
    driver = webdriver.Chrome(options=driverOptions)
    driver.get(set)
    time.sleep(1)
    data = driver.find_element(By.ID, "columnLeft").text.split("\n")
    fileStructure = data[0].replace("/", "").replace(":", "").split(" » ")
    filepath = constants.MAINPATH
    for folder in fileStructure:
        filepath += "/" + folder
        if fileStructure.index(folder) == len(fileStructure) - 1:
            open(filepath + ".csv", "w", encoding="utf-8").write("\n".join(data))
            break
        if not os.path.exists(filepath):
            os.mkdir(filepath)
    print(fileStructure)
    driver.quit()