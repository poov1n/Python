# call function at a particular interval of time and update the changes
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Importing modules from these is to run the code without *DEPRICATED WARNING* selenium.webdriver.common.by selenium.webdriver.chrome.service webdriver_manager.chrome

# For running the code in non depricated way use the below 3 lines of code
# import webdriver_manager
        # once imported and package delete the above line of code
#from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# s = Service(ChromeDriverManager().install())

on = True
while on:
    def five_seconds():
        time.sleep(5)
        cdp = "D:/stuff/chromedriver/chromedriver.exe"
        driver = webdriver.Chrome(executable_path=cdp)
        # Why we have to answer questions to make sure we are not robot
        driver.get("https://www.amazon.in/Homdum%C2%AE-speed-Drilling-Machine-Variable/dp/B08561QBYH/ref=sr_1_2_sspa?keywords=drill&qid=1669531391&qu=eyJxc2MiOiI1LjM3IiwicXNhIjoiNS40NCIsInFzcCI6IjQuODAifQ%3D%3D&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
        price = driver.find_element(By.CLASS_NAME, "apexPriceToPay")
        print(price.text)
        driver.quit()

    five_seconds()
    
# This would check the price every 5 seconds for all eternity as it is on an infinite loop
# make an if statement to see if the price is < a value, then email us or a text message saying the product is good to grab




