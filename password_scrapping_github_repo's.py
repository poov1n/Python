from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# https://github.com/usernam121

scrape = input("What GitHub page would you like to Scrape? - ")
cdp = "D:/stuff/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=cdp)

driver.get(f"{scrape}")
repo = f"{scrape}"

# time.sleep(2)
resource = driver.find_elements(By.CLASS_NAME, "repo") # Locating Class in the page
# time.sleep(2)

# Creating a FOR loop for printing repo's in the page

# for i in resource:
#    print(i.text)

# Clicking on an element (Click the tab on a pag to open a new one)
# make a list

links = []                       # used to store the resource values
webpages =[]                     # Used to store the new webpages by joining with the resource value
def going_for_raw(second_page):
    driver.get(second_page)      # Loading the second page in the browser
    raw = driver.find_element(By.CLASS_NAME, "js-permalink-replaceable-link")
    raw.click()                  # This would Click the raw button in the webpage
    html = driver.page_source    # Inspecting page source of that webpage
    html = f"{html}"
    if "password" in html:
        print(f"Found Password !!{second_page}")


def loop(first_page):            # Function to loop through the new pages searching for a specific value
    global a                     # Not a good practice in an organisation to make a variable as global in a code, but this is a sample tool.
    driver.get(first_page)
    time.sleep(3)
    resource2 = driver.find_elements(By.CLASS_NAME, "js-navigation-open")      # Class of next page
    for a in resource2:
        pass
#        print(a.text)
    if "py" in a.text:
        second_page = f"{first_page}/blob/main/{a.text}"
        going_for_raw(second_page)
#       print(second_page)



## We can scrape through the page by usuing various elements like below ##

#    elif "js" in a.text:
#       second_page = f"{first_page}/blob/main/{a.text}"
#    elif "php" in a.text:
#        second_page = f"{first_page}/blob/main/{a.text}"


for i in resource:
    links.append(i.text)
# print(links)

for l in links:
    first_page = f"{repo}/{l}"
    webpages.append(first_page)
    loop(first_page)

# print(webpages)

# Calling the first function


driver.quit()
