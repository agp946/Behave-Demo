from selene import browser
from selene import config
from selenium import webdriver

def before_all(context):
    config.timeout = 10
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    web_driver = webdriver.Chrome(executable_path="./resources/drivers/chromedriver.exe", options=options)
    browser.set_driver(web_driver)
    browser.open_url("http://automationpractice.com/index.php?controller=contact")

def after_all(context):
   browser.quit()



