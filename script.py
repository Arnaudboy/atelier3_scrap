from selenium import webdriver
from time import sleep
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

binary = "/Applications/Firefox.app/Contents/MacOS/firefox"

driver = webdriver.Firefox()
driver.get("https://boston.craigslist.org/search/boston-ma/cta#search=1~gallery~0~0")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'titlestring')))
test = driver.find_elements(By.CLASS_NAME, 'titlestring')
dict = {"links": [link.get_attribute('href') for link in test], "titles": []}
    
# for line in test:
#     #print(line.get_attribute('innerHTML'))
#     dict["links"].append(line.get_attribute('href'))
#     dict["titles"].append(line.get_attribute('innerHTML'))

for link in dict["links"]:
    driver.get(link)

driver.quit()