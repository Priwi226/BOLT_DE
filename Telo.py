#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 15:59:28 2023
 
@author: priwi
"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from colorama import init, Fore, Style
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
import time
import spravy
from prihlasenie import prihlasenie
import datetime
import os


def Telo(driver, Posledna_zakazka, Adresa_vyzdvyhnutia, Adresa_vylozenia, old_tab, Prehliadac_on):
    user_name = os.getlogin()
    Posledna_zakazka = None
    old_tab = None
    time.sleep(10)
    
    while True:
        
        # Hladanie textu No order ziskanie datumu a casu a nasledny print textu  
        ziadosti = driver.find_elements(By.XPATH, "//*[contains(text(), 'No orders')]")
        datum = datetime.datetime.today()
        cas = datetime.datetime.now().time()
        Aktualny_cas = cas.strftime("%H:%M:%S")
        print('\n' + Style.BRIGHT + "Hľadám nové BOLT objednávky " + Style.RESET_ALL + Aktualny_cas)

            # Ak Posledna zakazka obsahuje udaje a nieje None tak netlaci
        if Posledna_zakazka is not None:
           print("Posledná objednávka:\n  " + Posledna_zakazka)
           
        time.sleep(2)
            # ak sa text No ordner nenachadza v tabulke tak vykonava
    
        if len(ziadosti) == 0:
            print("po ==")
            # Nájdenie tabuľky pomocou className
                # Ak je tabulka pritona vykonava dalej 
            try:
                print("hladam tabulku")
                table_body = driver.find_element(By.XPATH, "//div[@data-kalep-component='table']//table")
                print("nensiel som tabulku")
                # Ak tabulka nieje pritomna tab ukonci browser nasledne ho otvore okno a vytvory nove prihlasenie 
            except NoSuchElementException:
                time.sleep(2)
                print("pred NAjdeny Refresh")
                spravy.me_send_to_telegram("hladam refresch BOLT")
                # refresh = driver.find_element(By.XPATH, "//button[contains(text(), \"Refresh\")]")
                # refresh = driver.find_element_by_css_selector(".__kalep.__kalep_1_1_44")
                # refresh = driver.find_element_by_xpath("//button[contains(@class, '__kalep') and contains(@class, '__kalep_1_1_44')]")
                driver.quit
                time.sleep(10)
                driver.get("https://fleets.bolt.eu/v2/57093/orders?tab=incoming-orders")
                spravy.me_send_to_telegram("sputsil som bol na novo")
                prihlasenie(driver)
                time.sleep(5)



                # print("NAjdeny Refresh")
                # print(refresh)
                # refresh.click()
                # print("Klikol som na Refresh")
                # time.sleep(2)
                # print("prechadzam na stranku")
                # driver.get("https://fleets.bolt.eu/v2/57093/orders?tab=incoming-orders")
                # print("Cakam 5 sekund")
                # time.sleep(5)
                
                
                try:
                    prihlasenie(driver)
                    driver.get("https://fleets.bolt.eu/v2/57093/orders?tab=incoming-orders")
                except:
                    continue
                    
                continue  # Pokračovať v cykle

            # Nájdenie riadkov tabuľky
            try:
                rows = table_body.find_elements(By.XPATH, ".//tbody/tr")
            except StaleElementReferenceException:
                continue
            
            if len(rows) == 0:
                continue
            
            time.sleep(1)
    
            neu_tab = []
    
            # Prechádzanie jednotlivých riadkov a získavanie údajov
            try:
                for riadok in rows:
                    bunky = riadok.find_elements(By.TAG_NAME, 'td')
                    datum_a_cas = bunky[0].text
                    sofer = bunky[1].text
                    meno_zakaznika = bunky[2].text
                    adresa_vyzdvyhnutia = bunky[3].text
                    neu_tab.append((datum_a_cas, sofer, meno_zakaznika, adresa_vyzdvyhnutia))
    
            except StaleElementReferenceException:
                driver.refresh()
                time.sleep(1)
                continue
    
            if old_tab == neu_tab:
                # Ak sa tabuľky zhodujú, pokračuje sa v ďalšom kóde
                time.sleep(3)
                print("Tabuľky sa zhodujú. Nevykonávam žiadnu akciu.")
                continue
            else:
                # Ak sa tabuľky nezhodujú, vykonávajú sa príslušné akcie
                print("Zmena v tabuľke. Vykonávam príslušné akcie.")
    
                for riadok in neu_tab:
                    datum_a_cas = riadok[0]
                    sofer = riadok[1]
                    meno_zakaznika = riadok[2]
                    adresa_vyzdvyhnutia = riadok[3]
    
                old_tab = neu_tab
                datum = datetime.date.today()
                cas = datetime.datetime.now().time()
                Aktualny_cas = cas.strftime("%H:%M:%S")
                print('\033[1m' + "     Nájdená nová objednávka     " + '\033[0m' + Aktualny_cas)
                
                    #   Vytvorenie linku pre startovaciu adresu 
                start_link = ("http://maps.google.com/maps?q=" + adresa_vyzdvyhnutia)
                
                
                    #   Vytvorenie Telegramovej pravy
                telegram_message = (
                    "<b>" + sofer + "</b>\n"  + "BOLT" + " €      " + "\n" + "<a href='" + start_link + "'>" + adresa_vyzdvyhnutia + 
                    "</a>\n ---------> \n" 
                    + meno_zakaznika
                )        
                
                # Vytvorenie udajov pre knihu jazd 
                Kniha_jazd = (
                    str(datum) + " ; " + str(cas) + " ; " + str(adresa_vyzdvyhnutia) + " ; BOLT Ziel adresse ; " +
                    str(sofer)  + " ; BOLT vzdialenost  ; BOLT vzdialenost ; Master "
                    )
                
                # Zapis do knihy jazd 
                with open("Auftrags_aufzug.txt", "a") as file:
                    file.write(Kniha_jazd + "\n")  # Zápis dát do súboru
                
                
                # Odosielanie telegram sprav 1) skupina sofery 
                # Odosielanie telegram sprav 2) Unthenehmer skupina 
                spravy.me_send_to_telegram(telegram_message)
                spravy.send_to_telegram_with_timer(telegram_message) 
                
            old_tab = neu_tab
    
            # Vytvorenie premennej na zaklade ziskanych udajov
            Posledna_zakazka = ( 
                    datum_a_cas + "  " + sofer + " " + adresa_vyzdvyhnutia
                    )
            time.sleep(2)
            continue
                