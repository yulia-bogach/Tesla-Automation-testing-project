# Helpers file for project Tesla (Personal Address book)
import time
import random
import requests
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
import credentials as cr

faker_class = Faker()

# Set main variables
# URL - home page
main_url = "https://www.tesla.com/"

# User's E-mail
user_email = "..."  # type your user's E-mail for account
# User's password
user_pass = "..."  # type your user's password for account

# Invalid email
inv_email = "..."  # type your inv E-mail for account
# Ad Hoc email
adhoc_email = "..."  # type your adhoc E-mail for account


# driver sleep from 1 to 3, or 1 to 5 seconds
def delay1_3():
    time.sleep(random.randint(1, 3))

def delay1_5():
    time.sleep(random.randint(1, 5))



