from time import sleep
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


gif = input("Enter gif link: ")

opt = Options()
opt.add_argument("--start-maximized")
# opt.add_argument("-headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opt)
driver.implicitly_wait(10)

driver.get("https://ezgif.com/resize")

driver.find_element_by_class_name("text").send_keys(gif)
sleep(0.5)

driver.find_element_by_xpath('//*[@id="tool-submit-button"]/input').click()
sleep(2)

box = driver.find_element_by_xpath('//*[@id="width"]')
box.send_keys("45")
box.send_keys(Keys.ENTER)

link = driver.find_element_by_xpath('//*[@id="output"]/p[1]/img').get_attribute('src')
sleep(1)

driver.get("https://imgur.com/upload")

box = driver.find_element_by_xpath(
    '//*[@id="root"]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/input')
box.send_keys(link)
box.send_keys(Keys.ENTER)

sleep(2)
driver.find_element_by_xpath(
    '//*[@id="root"]/div/div[1]/div/div[4]/div[2]/div/div[3]/div[4]/button').click()
