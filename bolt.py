#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:58:17 2023

@author: priwi
"""


from selenium import webdriver
from prihlasenie import prihlasenie
from Telo import Telo
import traceback
import selenium
from selenium.webdriver.chrome.options import Options
from Telo import Telo
import spravy
import os 
import Nadstavenia
import time


telegram_mess = "RUF GLEICH ZUM CHEF. Auftrags system ist runtergefalen !!!!!! BOLT" 

user_name = os.getlogin()

chrome_driver = f"/home/{user_name}/chromedriver"
#chrome_driver = ()
os.system (f"rm -rf __pycache__")

Prehliadac_on = 0




try:
    if Nadstavenia.Prehliadac_on == 1:
        # driver = webdriver.Chrome(chrome_driver)
        driver = webdriver.Firefox()
    elif Prehliadac_on != 1:
        options = Options()
        options.add_argument("--headless")  # Nastavenie pre bezhlavý režim
        driver = webdriver.Chrome(chrome_driver, options=options)
        
    driver.get("https://fleets.bolt.eu/v2/57093/orders?tab=incoming-orders")
    time.sleep(5)
    
    prihlasenie(driver)
    Posledna_zakazka = None
    Adresa_vyzdvyhnutia = None
    Adresa_vylozenia = None
    old_tab = None

    
    Telo(driver, Posledna_zakazka, Adresa_vyzdvyhnutia, Adresa_vylozenia, old_tab, Prehliadac_on)

except Exception as e:
    # Ak nastane zlyhanie, zaznamenajte chybovú správu
    error_message = str(e)
    
    # Získanie posledných dvoch riadkov kódu
    code_lines = traceback.format_exc().strip().split('\n')
    last_two_lines = code_lines[-3:]
    code_snippet = "\n".join(last_two_lines)
    error_message_with_code = f"{code_snippet}\n\n{error_message}"
    #driver.quit()
    
    # Odoslanie Telegram správy s chybovou hláškou a výpisom kódu
    spravy.me_send_to_telegram(telegram_mess + "\n\n" + error_message_with_code)
    # send_to_telegram(telegram_mess + "\n\n" + error_message_with_code)
    print(telegram_mess + "\n\n" + error_message_with_code)
    # print(error_message_with_code)
    
    # Získanie informácií o problematickom prvku
    element_info = ""
    if isinstance(e, selenium.common.exceptions.StaleElementReferenceException):
        element = driver.find_element_by_id("id_prvku")  # Nahraďte "id_prvku" skutočným identifikátorom prvku
        element_info = f"Prvok: {element.tag_name} s id={element.get_attribute('id')} a class={element.get_attribute('class')}"
        print("Informácie o problematickom prvku:")
        print(element_info)

    # Zápis do súboru Log.txt
    log_message = f"{telegram_mess}\n\n{error_message_with_code}\n\n{element_info}"
    with open("Log.txt", "w") as file:
        file.write(log_message)
    input("Stlac Enter pre ukončeníe...")
    #driver.quit()


