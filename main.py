from selenium import webdriver

driver = webdriver.Firefox()

#Create a test which logs in to https://front-stage.cashortrade.org

driver.get("https://front-stage.cashortrade.org")



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