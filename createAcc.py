from selenium import webdriver

import random
import string
import time
driver = webdriver.Chrome()

def RandoString (len=8):
    result = string.ascii_lowercase+string.digits
    return ''.join(random.choice(result) for i in range(len))

def makeAcc(u,p):
    driver=webdriver.Chrome("C:/Users/12512/PycharmProjects/AutomateRs/chromedriver.exe")
    driver.get('https://oldschool.runescape.com/')
    driver.find_element_by_id('signup').click()
    time.sleep(15)
    driver.find_element_by_name('email1').send_keys(u)
    driver.find_element_by_name('password1').send_keys(p)
    driver.find_element_by_name('day').send_keys('01')
    driver.find_element_by_name('month').send_keys('01')
    driver.find_element_by_name('year').send_keys('1995')
    driver.find_element_by_id('create-submit').click()
    time.sleep(5)


def main():

    username = RandoString().__add__('@gmail.com')
    password = RandoString(10)
    makeAcc(username,password)
    with open('cred-file.txt','a+') as new_file:
        new_file.write('Username: '+ username + ' | Password: ' + password +'\n')



main()