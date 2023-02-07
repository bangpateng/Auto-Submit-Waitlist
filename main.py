import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

website = input("Masukan Link Website: ")
print("Link website yang dimasukkan:", website)
email_xpath = input("Masukan Xpath 1: ")
print("Xpath email yang dimasukkan:", email_xpath)
submit_xpath = input("Masukkan Xpath 2: ")
print("Xpath submit yang dimasukkan:", submit_xpath)
time.sleep(1)

def mulai():
    data = pd.read_csv('emaildata.csv')
    recycle = data.shape[0]
    for i in range(recycle):
        print(i)
        driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(), "chromedriver.exe"))
        driver.get(website)
        time.sleep(3)

# Isi Email Otomatis
        email = data.iloc[i]['email']
        input_email = driver.find_element(By.XPATH, email_xpath)
        for j in email:
            input_email.send_keys(j)
            time.sleep(0.05)

# Klik Button
        submit = driver.find_element(By.XPATH, submit_xpath)
        submit.click()
        time.sleep(0.5)

mulai()
time.sleep(10)
