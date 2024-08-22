#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 07:38:28 2023

@author: priwi
"""




nastup = 4 
cena_km = 1.18
cena_cas = 0.30 


Prehliadac_on = 1 # 1 spusteny prehliadac 
#Google_on_api = 1 if dnes % 2 == 0 else 0 #kazdy parny den
Google_on_api = 1 #### 1 zapnut
schedule_time_on = 1
Zvyhodneny_sofer_on = 1 # 1 = zapnute
Vyluceny_sofer_casovka_on = 1 # 1 = zapnute 

KNIHA_JAZD = 1  # 0 vypnute

###         Podmienky
Min_cena = 0
Max_cena = 100000 
Min_km = 0
Max_km = 100

###################################### 
A = Alianz = [80939, 89451, 23665]
M = Messe =  [81829, 81823, 85609]
L = Lilienalle = [80939]
O = Olympia = [80809]
PSC_vyzdvyhnutia = ()
PSC_cielu = ()


######################################################
Vyluceny_sofer = ["Peter", "Jozko"]

Zvyhodneny_sofer = {
    "Peter": 20,
    "Nikol": 1,
    "Marek": 8,
    }


###         Stroj
STROJ = ("Master")

###         Prihlasovanie na stranku
MENO = ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
HESLO = ("xxxxxxxxxxxxxxxxxxxxx!")

Odmlka = int(5)

###         Telegram Data
Telegram_api_Token_uber = ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
Telegram_api_Token_kiwi = ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
Telegram_miestnost_kiwi = ("xxxxxxxxxxxxxxx")  #---- KIWI
Telegram_miestnost_uber = ("xxxxxxxxxxxxxxx")  #---- Auftrags
Telegram_miestnost_ja = ("xxxxxxxxxxxxxx")  #---- Uber zakazky
URL = ("f'https://api.telegram.org/bot{apiToken}/sendMessage'")
Telegram_mazanie = "300"


###         SMS data
Sms_kluc = ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

##FTP Nadstavenia 
Download_add = ("/home/priwi/Stiahnuté")

FTP_NAME = ("xxxxxxxxxxxxxx")
FTP_MENO = ("xxxxxxxxxx")
FTP_HESLO = ("xxxxxxxxxx")
FTP_Cesta = ("/Python")
FTP_SUBOR = ("Uber_clicker.txt")
FTP_cas = 63

Nazov_subory =("driver_performance.csv")

####        Definovanie slov
Povodny_nazov_obsahuje = ("Driver Quality")
slovo = ("Kvalita vodiča")



###### Email nadstavenia
SMTP = ("smtp")
IMAP = ("imap")
Email_meno = ("xxxxxxxxxxxxxxx")
Email_heslo = ("xxxxxxxxxxxxxxxxx")
Odosielatel = ("xxxxxxxxxxxxxxxxxxx")
Predmet = ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


####   Google API
Googleapi =  ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

Casovy_rozvrh = {
    "monday": {
        '04:00-05:00': 26.99,
        '05:00-07:00': 24.5,
        '07:00-08:00': 15.21,
        '08:00-09:00': 25.14,
        '09:00-12:00': 15.78,
        '12:00-19:00': 15.60,
        '19:00-20:00': 18.45
    },
    "tuesday": {
        '04:00-08:00': 16.34,
        '08:00-11:00': 11.65,
        '11:00-16:00': 15.6,
        '16:00-17:00': 17.29,
        '17:00-19:00': 14.29,
        '19:00-20:00': 12.59,
    },
    "wednesday": {
        '04:00-05:00': 21.92,
        '05:00-06:00': 26.14,
        '06:00-07:00': 25.15,
        '07:00-08:00': 23.04,
        '08:00-12:00': 15.21,
        '12:00-13:00': 14.63,
        '13:00-15:00': 13.96,
        '15:00-18:00': 16.85,
        '18:00-19:00': 14.83,
        '19:00-20:00': 11.71
    },
    "thursday": {
        '06:00-07:00': 19.42,
        '07:00-11:00': 17.05,
        '11:00-12:00': 25.9,
        '12:00-16:00': 15.46,
        '16:00-17:00': 18.22,
        '17:00-18:00': 15.09,
        '18:00-19:00': 15.75,
        '19:00-20:00': 15.36
    },
    "friday": {

        '00:00-05:00': 15.09,
        '05:00-06:00': 18.01,
        '06:00-07:00': 20.36,
        '07:00-08:00': 22.16,
        '08:00-11:00': 16.82,
        '11:00-12:00': 14.45,
        '13:00-19:00': 18.07,
        '19:00-23:00': 12.73,
        '23:00-23:59': 15.16
    },
    "saturday": {
        '00:00-01:00': 15.78,
        '01:00-02:00': 15.57,
        '02:00-03:00': 15.73,
        '03:00-04:00': 17.07,
        '04:00-05:00': 15.92,
        '05:00-07:00': 15.00,
        '07:00-09:00': 15.84,
        '09:00-18:00': 15.63,
        '18:00-19:00': 15.09,
        '19:00-20:00': 15.06,
        '20:00-22:00': 16.22,
        '22:00-23:59': 15.49,
    },
    "sunday": {
        '00:00-04:00': 15.79,
        '04:00-05:00': 15.62,
        '05:00-09:00': 15.00,
        '09:00-10:00': 15.85,
        '10:00-11:00': 15.66,
        '11:00-17:00': 15.00,
        '17:00-18:00': 15.37,
        '18:00-19:00': 15.86,
        '19:00-20:00': 15.19,
    }
}



test = 0


