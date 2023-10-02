# -*- coding: utf-8 -*-
# Splitting the text using the specified delimiter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
import pyperclip
import os
import time
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import urllib.request
import json,re,string

# URL = "你的网址"  # 替换成你需要访问的网页的URL
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException

# URL = "你的网址"  # 替换成你需要访问的网页的URL
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
# 启动Chrome浏览器
# driver = webdriver.Chrome(executable_path=r"C:\Users\Morning\Desktop\hiwi\爬虫\chromedriver.exe")  # 修改为你的chromedriver的实际路径
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options,executable_path=r"C:\Users\Morning\Desktop\hiwi\爬虫\chromedriver.exe")
# 找到输入框并输入变量a
"""
cd C:\Program Files\Google\Chrome\Application
chrome.exe --remote-debugging-port=9222 --disable-web-security --user-data-dir=remote-profile   
"""
# if "There was an error generating a response" in driver.page_source:
#     print("tyue")
def scroll_to_end():
    total_height = int(driver.execute_script("return document.body.scrollHeight;"))

    # 设置每次滚动的距离和等待时间
    increment = random.randint(1500,2500)
    wait_time = random.uniform(0.3,0.6)
    current_position = driver.execute_script("return window.pageYOffset;")

    # 开始缓慢滚动
    while current_position < total_height:
        current_position += increment
        driver.execute_script(f"window.scrollTo(0, {current_position});")
        time.sleep(wait_time)

        # 更新 total_height，因为有些页面在滚动时可能会加载更多内容
        total_height = int(driver.execute_script("return document.body.scrollHeight;"))
