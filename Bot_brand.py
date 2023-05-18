from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


#### Getting page url ####
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(
    options=options, executable_path=r'./chromedriver.exe')
driver.maximize_window()
# driver.get("https://www.meinprospekt.de/filialen/real-de")
driver.get("https://www.meinprospekt.de/filialen/aldinord-de")


#### Getting ID numbers ####
# df1 = pd.read_csv("ID.csv")
# ID = df1.url
Name_list = []
Street_List = []
City_list = []
result_list = []
new_data = {}

for i in range(1, 11):
    try:
        driver.find_element(By.XPATH, f'//*[@id="mp-main"]/div[3]/div[2]/a[{i}]').click()
    except:
        continue
    tables = driver.find_elements(By.XPATH, '//*[@id="mp-main"]/div[3]/ul/li/a')
    for table in tables:
        Name = table.find_element(By.TAG_NAME, 'strong').text   
        Name_list.append(Name)
        new_data["Name"] = Name
        print(Name)

        Addresses = table.find_elements(By.TAG_NAME, 'span')
        Address = Addresses[1].find_elements(By.TAG_NAME, 'span')
        Street = Address[0].text
        Street_List.append(Street)
        new_data["Street"] = Street
        print(Street)
        
        Zip = Address[1].text
        address = Address[2].text  
        City = Zip + " " + address   
        City_list.append(City)
        new_data["City"] = City
        print(City)

        result_list.append(new_data)

        dict = {'Name': Name_list, 'Street': Street_List, 'City': City_list}

        df = pd.DataFrame(dict)

        df.to_csv('Result.csv')
print(result_list)
while True:
    pass
