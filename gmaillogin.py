﻿from selenium import webdriver

driver=webdriver.Chrome('D:\\Browser Drivers\\chromedriver.exe')
driver.set_page_load_timeout(30)
driver.get('https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier')
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_id('Email').send_keys('rchennale')
driver.implicitly_wait(5)
driver.find_element_by_id('next').click()
driver.implicitly_wait(5)
driver.find_element_by_id('Passwd').send_keys('9902602832')
driver.implicitly_wait(5)
driver.find_element_by_id('signIn').click()
print('login successfully')
driver.implicitly_wait(20)
webdriver.Chrome()
print()