import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
driver.get("https://kite.zerodha.com/holdings")
driver.maximize_window()
username = driver.find_element_by_id("userid").send_keys("MY3129")
driver.implicitly_wait(1500)
password = driver.find_element_by_id("password").send_keys("shivaraj@876")
driver.implicitly_wait(2000)
submit = driver.find_element_by_xpath(("//button[contains(text(),'Login')]")).submit()
driver.implicitly_wait(1500)
password = driver.find_element_by_id("pin").send_keys("872283")
driver.implicitly_wait(1000)
submit = driver.find_element_by_xpath("//button[contains(text(),'Continue')]").submit()
time.sleep(10)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)

driver.set_window_size(S('Width'), S('Height'))

driver.find_element_by_tag_name('body').screenshot('./HoldingsFull.png')
