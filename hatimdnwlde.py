from selenium import webdriver
import string
import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser

Path = "D:\webdriver\\chromedriver.exe"
driver = webdriver.Chrome(Path)
driver.switch_to.window(driver.window_handles[0])

driver.get("https://azee5.blogspot.com/2019/07/hatim-2003-serial-all-episodes-free.html?m=1")
while(True):
    a=input()
    if a=="ok":
        break
j=0
k=driver.find_elements_by_partial_link_text("Mega")
print(k)
p=[]
for i in k:
    j=j+1
    if j>42:
     p.append(i)

print(len(p))
j=0
for i in p:
    print(j+1)
    j=j+1
    i.click()

    time.sleep(3)
    winoafter=driver.window_handles[j]
    driver.switch_to.window(winoafter)
    time.sleep(13)
    try:
     l = driver.find_element_by_xpath("//div[@class='download big-button button download-file green transition']")
     l.click()
     time.sleep(2)
     driver.switch_to.window(driver.window_handles[0])
    except:
        pass

