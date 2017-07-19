#chrome-extension://phldilnakifhbgllkiopclbdchkdcfoc/index.html
#chrome-extension://mbopgmdnpcbohhpnfglgohlbhfongabi/options.html
import time
from selenium import webdriver


import urllib.request
from  bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#
# chrome = webdriver.Chrome('D:\chromedriver/chromedriver.exe')
# time.sleep(5)


chop = webdriver.ChromeOptions()

chop.add_extension("D:\chromedriver/phldilnakifhbgllkiopclbdchkdcfoc.crx")

# create new Chrome driver object with blazemeter extension

chrome = webdriver.Chrome('D:\chromedriver/chromedriver.exe',chrome_options=chop)
chrome.get("chrome-extension://phldilnakifhbgllkiopclbdchkdcfoc/index.html")
time.sleep(5)
chrome.find_element_by_css_selector(".view-more-link").click()
time.sleep(5)
chrome.find_element_by_css_selector(".layout.thumbs").click()
# 반복할 횟수
chrome.find_element_by_xpath("//body").send_keys(Keys.END)
time.sleep(15)
chrome.find_element_by_xpath("//body").send_keys(Keys.END)
time.sleep(15)
chrome.find_element_by_xpath("//body").send_keys(Keys.END)
time.sleep(15)

chrome.find_element_by_css_selector("button.alt").click()
time.sleep(15)


chrome.find_element_by_xpath("//body").send_keys(Keys.END)
time.sleep(15)
chrome.find_element_by_xpath("//body").send_keys(Keys.END)
time.sleep(15)
chrome.find_element_by_xpath("//body").send_keys(Keys.END)
time.sleep(15)

chrome.find_element_by_css_selector("button.alt").click()
time.sleep(15)


chrome.find_element_by_xpath("//body").send_keys(Keys.END)
time.sleep(15)
chrome.find_element_by_xpath("//body").send_keys(Keys.END)
time.sleep(15)
chrome.find_element_by_xpath("//body").send_keys(Keys.END)
time.sleep(15)

chrome.find_element_by_css_selector("button.alt").click()
time.sleep(15)


chrome.find_element_by_xpath("//body").send_keys(Keys.END)
time.sleep(15)
chrome.find_element_by_xpath("//body").send_keys(Keys.END)
time.sleep(15)
chrome.find_element_by_xpath("//body").send_keys(Keys.END)
time.sleep(15)

chrome.find_element_by_css_selector("button.alt").click()
time.sleep(15)
