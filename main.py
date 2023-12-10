from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()

driver.implicitly_wait(15)

#Create a test which logs in to https://front-stage.cashortrade.org

driver.get("https://front-stage.cashortrade.org")

#Xpath specs https://www.w3.org/TR/xpath-30/
# section 3.2 , dynamic processing
driver.find_element(By.XPATH, '/descendant::*[text() = "Log In"]').click()

sleep(1)

#with phone number (888) 888-8888
phone_box = driver.find_element(By.XPATH, '/descendant::input[attribute::type ="tel"]')
phone_box.click()
phone_box.send_keys("8888888888")
driver.find_element(By.XPATH, '/descendant::*[text() = "Next"]').click()

#2auth code will be: 000000
auth_box = driver.find_element(By.XPATH, '/descendant::input[attribute::autocomplete ="one-time-code"]')
auth_box.send_keys("000000")
driver.find_element(By.XPATH, '/descendant::*[text() = "Next"]').click()

driver.find_element(By.XPATH, '/descendant::*[text() = "Sell Tickets"]').click()
driver.find_element(By.XPATH, '/descendant::*[text() = "Skip Walkthrough"]').click()
driver.find_element(By.XPATH, '/descendant::button[attribute::id = "performer-result-2"]').click()
driver.find_element(By.XPATH, '/descendant::button[attribute::id = "search-event-result-0"]').click()

driver.find_element(By.XPATH, '/descendant::button[attribute::id = "sellortrade-sell"]').click()
driver.find_element(By.XPATH, '/descendant::*[text() = "Digital Transfer"]/ancestor::button').click()
sleep(5)
driver.find_element(By.XPATH, '/descendant::*[text() = "Next"]/ancestor::button').click()
'''
Create a test which logs in to https://front-stage.cashortrade.org with phone number (888) 888-8888
2auth code will be: 000000
Pick any random artist from the main search page and create a sale post for it
Transfer ready: I'm ready
Section: GA 
Subsection: Balcony
Selected option for tickets value: Face value
Selected price: 12 USD
If any other options I haven't specified, just pick one (it won't change the flow)
Add a test payment card: 4242424242424242 expiration is any future date, this date must be today + 1 year
Paypal connect is not necessary 
Finally submit the listing 
Expected result: I should head to this account and see this newly created listing as active and ready to accept offers.
'''