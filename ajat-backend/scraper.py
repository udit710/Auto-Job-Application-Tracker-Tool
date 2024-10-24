from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import os

def handle_login(username, password, driver):
    # Open LinkedIn login page
    driver.get('https://www.linkedin.com/login')

    time.sleep(2)  # time for the page to load

    email_input = driver.find_element(By.ID, "username")
    email_input.send_keys(username)
    
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)

    # Submit the form
    password_input.send_keys(Keys.RETURN)
    time.sleep(2)  # time for the page to submit

def scrape_job_description(job_link):

    service = Service(os.getenv('CHROMEDRIVER')) 
    driver = webdriver.Chrome(service=service) # start chromedriver service
    
    # Only for LinkedIn
    if 'linkedin' in job_link:

        email = os.getenv('PORTALUSERNAME')
        password = os.getenv('PORTALPASSWORD')
        
        handle_login(email, password, driver) # pass the same driver instance to the login function

    driver.get(job_link)
    time.sleep(5)  # Allow time for the page to load

    # parse the job body
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    job_description = soup.find('body')

    driver.quit()
    
    # Extract text from the body
    if job_description:
        description_text = job_description.get_text(separator=",")
        return description_text
    else:
        return None

