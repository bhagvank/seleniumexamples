'''
Created on Mar 30, 2021

@author: bhagvan.kommadi
'''

from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case starting now")  
 
driver.maximize_window()  
  
driver.delete_all_cookies()  
 
driver.get("http://localhost:5000")

driver.find_element_by_xpath("//a[contains(text(),'Add Customer')][1]").click()  
time.sleep(4) 


driver.find_element_by_xpath("//input[@type='text'][@name='name'][1]").send_keys("Jack Hill")
  
time.sleep(2) 
driver.find_element_by_xpath("//input[@type='email'][@name='email'][1]").send_keys("jack@gmail.com")
  
time.sleep(2) 

driver.find_element_by_xpath("//input[@type='text'][@name='address'][1]").send_keys("345 Hill Drive, Sanjose 30489")
  
time.sleep(2) 

driver.find_element_by_xpath("//input[@type='submit'][@value='Submit'][1]").click()
  
time.sleep(2) 

 
driver.close()  
print("Customer creation")
