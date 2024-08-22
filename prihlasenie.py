#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:57:23 2023

@author: priwi
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import re
import time
import requests
from datetime import datetime

MENO = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
HESLO = "xxxxxxxxxxxxxxxxxxxxxxxxxx"

def prihlasenie(driver):
    
    time.sleep(2)
    try:
        Prihlasenie_email = driver.find_element(By. ID, "email")
        Prihlasenie_email.send_keys(MENO)
        Prihlasenie_heslo = driver.find_element(By. ID, 'current-password')
        Prihlasenie_heslo.send_keys(HESLO)
    except:
        print("Nenasiel som polia:\nID: email\nID: current-password")
    
    try:
        cookies = driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]")
        cookies.click()
    except:
        try:
            cookies = driver.find_element(By.XPATH, "//button[contains(text(), 'Prijať')]")
            cookies.click()
        except:
            print("Nenasiel som tlacidlo Akcepted pre cookies")
            
        print("Nenasiel som tlacidlo Akcepted pre cookies")
    
    time.sleep(2)
    try:
        Prihlasenie_button = driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]")
        Prihlasenie_button.click()
    
    except:
        print("Nenasiel som tlacidlo na prihlasenie. Respektive som zle klikol")
    
    time.sleep(4)
    
    
    try:
        LetsGo = driver.find_element(By.XPATH, "//button[contains(text(), \"Let's Go\")]")
        LetsGo.click()
    except:
        print("Nenasiel som tlacidlo Lets's Go")
