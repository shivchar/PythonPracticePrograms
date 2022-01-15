from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://kite.zerodha.com/holdings")
driver.maximize_window()
username=driver.find_element_by_id("userid").send_keys("MY3129")
driver.implicitly_wait(1500)
password=driver.find_element_by_id("password").send_keys("shivaraj@876")
driver.implicitly_wait(2000)
submit=driver.find_element_by_xpath(("//button[contains(text(),'Login')]")).submit()
driver.implicitly_wait(1500)
password=driver.find_element_by_id("pin").send_keys("872283")
driver.implicitly_wait(1000)
submit=driver.find_element_by_xpath("//button[contains(text(),'Continue')]").submit()
