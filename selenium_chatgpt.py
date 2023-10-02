# -*- coding: utf-8 -*-
# Splitting the text using the specified delimiter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
import urllib.request
# URL = "你的网址"  # 替换成你需要访问的网页的URL
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
import urllib.request
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

def next_topic_func():
    next_topic_str='//*[@id="__next"]/div[1]/div[1]/div/div/div/nav/div[1]/a'
    button_confirm = driver.find_element_by_xpath(next_topic_str)
    driver.execute_script("arguments[0].click();", button_confirm)
def exception_handling():
    if "There was an error generating a response" in driver.page_source:
        return "next_topic"
    try:
        print("尝试点击relative_select")
        relative_select = '//*[@id="__next"]/div[1]/div[2]/div/main/div[1]/div[1]/div/div/div/div/div/div[2]/div/div/button[1]'

        # relative_select='//*[@id="__next"]/div[1]/div[2]/div/main/div[1]/div[1]/div/div/div/div[4]/div/div[2]/div/div/button[1]'
        button_confirm = driver.find_elements_by_xpath(relative_select)[-1]
        driver.execute_script("arguments[0].click();", button_confirm)
    except:
        pass
    try:
        print("尝试点击acknowledge")
        button = driver.find_element_by_xpath("//div[text()='Acknowledge']")
        button.click()
        return "acknowledge"
    except:
        pass
def selenium_spider( input_str="",continully=True,next_topic=False):
    if not next_topic:

        input_str=input_str[:25000]
        if continully:
            # print(continully)
            input_element = driver.find_element(By.XPATH, '//*[@id="prompt-textarea"]')

            driver.execute_script("arguments[0].value = arguments[1];", input_element, input_str)
            sleep_time = random.uniform(1, 3)
            time.sleep(sleep_time)
                # time.sleep(1)
            driver.execute_script(
                    "var evt = document.createEvent('HTMLEvents'); evt.initEvent('input', true, true); arguments[0].dispatchEvent(evt);",
                    input_element)#触发input效果33
            # input_element.send_keys("\n")
                # length = len(ii)
                # # 以每次100个字符遍历字符串
                # for i in range(0, length, 700):
                #     # 获取当前位置到下一个100个字符的子字符串
                #     substring = ii[i:i + 700]
                #     input_element.send_keys(substring)  # 你可以替换为变量a的值
            button_str='//*[@id="__next"]/div[1]/div[2]/div/main/div[1]/div[2]/form/div/div[2]/div/button'
            button_confirm=driver.find_element_by_xpath(button_str)
            driver.execute_script("arguments[0].click();", button_confirm)
        else:
            edit_str_ = '//*[@id="__next"]/div[1]/div[2]/div/main/div[1]/div[1]/div/div/div/div[3]/div/div/div[2]/div[2]'
            text_area = '//*[@id="__next"]/div[1]/div[2]/div/main/div[1]/div[1]/div/div/div/div[3]/div/div/div[2]/div/textarea'
            scroll_xpath = '//*[@id="__next"]/div[1]/div[2]/div/main/div[1]/div[1]/div/div/div/div[1]/div/div/div[1]/div[1]/div/img'
            while True:
                try:
                    driver.execute_script("window.scrollTo(0, 0);")
                    edit_button = driver.find_element_by_xpath(edit_str_)
                    scroll_place = driver.find_element_by_xpath(scroll_xpath)
                    driver.execute_script("arguments[0].scrollIntoView();", scroll_place)
                    edit_button.click()
                    textarea = driver.find_element_by_xpath(text_area)


                    # 如果点击成功，则跳出循环
                    break
                except Exception  as e:
                    # 如果发生异常，打印异常信息，并等待1秒后再次尝试
                    print(f"An error occurred: {e}, retrying...")
                    exception_feedback=exception_handling()
                    if exception_feedback=="acknowledge":
                        return "error violate rules"
                    elif exception_feedback=="next_topic":
                        return "next_topic"
                    driver.execute_script("window.scrollTo(0, 0);")
                    edit_button = driver.find_element_by_xpath(edit_str_)
                    scroll_place = driver.find_element_by_xpath(scroll_xpath)
                    driver.execute_script("arguments[0].scrollIntoView();", scroll_place)
                    edit_button.click()
                    # driver.execute_script("arguments[0].click();", remove_button)
                    sleep_time = random.uniform(1, 3)
                    time.sleep(sleep_time)

            # 清空<textarea>元素
            textarea.clear()
            # for ii in input_str.split("\n"):
            driver.execute_script("arguments[0].value = arguments[1];", textarea, input_str)
            sleep_time = random.uniform(1, 3)
            time.sleep(sleep_time)
            driver.execute_script(
                    "var evt = document.createEvent('HTMLEvents'); evt.initEvent('input', true, true); arguments[0].dispatchEvent(evt);",
                    textarea)

            textarea.send_keys("\n")
            submit_button_xpath = '//*[@id="__next"]/div[1]/div[2]/div/main/div[1]/div[1]/div/div/div/div[3]/div/div/div[2]/div/div/button[1]'
            submit_button = driver.find_element(By.XPATH, submit_button_xpath)
            driver.execute_script("arguments[0].click();", submit_button)
            # while True:
            #     try:
            #         # 查找按钮并点击
            #         submit_button = driver.find_element_by_xpath(submit_button_xpath)
            #         submit_button.click()
            #
            #         # 如果点击成功，则跳出循环
            #         break
            #     except (ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException) as e:
            #         # 如果发生异常，打印异常信息，并等待1秒后再次尝试
            #         print(f"An error occurred: {e}, retrying...")
            #         time.sleep(1)

        xpath_str = '//*[@id="__next"]/div[1]/div[2]/div/main/div/div[1]/div/div/div/div/div/div/div[2]/div[1]/div/div'
        # //*[@id="__next"]/div[1]/div gpt3
        # //*[@id="__next"]/div[1]/div[2] gpt4
        element_xpath_indication = '//*[@id="__next"]/div[1]/div[2]/div/main/div/div[2]/form/div/div[1]/div/div[2]/div/button/div'

        indication = "generate"
        text = None
        sleep_time = random.uniform(1, 3)
        time.sleep(sleep_time)
        while indication != "Regenerate":
            # print(indication)
            try:
                elements = driver.find_elements_by_xpath(xpath_str)
                text = elements[-1].text
                indication = driver.find_element_by_xpath(element_xpath_indication).text


            except (NoSuchElementException, StaleElementReferenceException) as e:
                print(e,"Element not found. Retrying...")

                sleep_time = random.uniform(1, 3)
                time.sleep(sleep_time)
                exception_feedback=exception_handling()
                if exception_feedback == "acknowledge":
                    return "error violate rules"
                elif exception_feedback == "next_topic":
                    return "next_topic"
        # print(element_xpath)

        # print(text)
        return text
    else:
        next_topic_func()

# print(selenium_spider("中俄罗斯两国因为国家边界问题争论不休",False))