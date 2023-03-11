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

cdp = "D:/stuff/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=cdp)

# Why we have to answer questions to make sure we are not robot
# Note than we need to inspect the pages and do trial and error of the "class" parameter which we are giving so that the code would output us with the right object 

driver.get("https://www.amazon.in/Homdum%C2%AE-speed-Drilling-Machine-Variable/dp/B08561QBYH/ref=sr_1_2_sspa?keywords=drill&qid=1669531391&qu=eyJxc2MiOiI1LjM3IiwicXNhIjoiNS40NCIsInFzcCI6IjQuODAifQ%3D%3D&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
price = driver.find_element(By.CLASS_NAME, "apexPriceToPay")
print(price.text)

driver.quit()

