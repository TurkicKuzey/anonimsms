#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import system as s

import os

os.system("pip install requests")

os.system("apt-get update")

os.system("apt-get upgrade")

os.system("apt-get install curl")
           
os.system("apt-get install python")
           
os.system("apt-get install figlet")

os.system("clear")

os.system("figlet SMS GONDERME ARACI")

banner = """
    > Coder BY discord.gg/turkism / Türkic Kuzey <
>İstediğiniz Telefon Numarasına Bir Günde Bir Mesaj Atma Hakkınız Vardır!
>Mesajınızdaki Karakter Sayısı 70'i Geçmemelidir.
>Telefon Numarasını Doğru Girmezseniz Hata Vericektir.
>Çalıştığını Onaylamak İçin Kendinizde Deneyebilirsiniz.
>Doğru Girdiğiniz Halde Hata Veriyorsa 2. Defa Tekrar Deneyin Hata Verse Bile Çalışacaktır.
>Discord: https://discord.gg/turkism
>Discorddaki Sunucumuza Katılmayı Unutmayın!
"""

print(banner)

sor = input("Telefon Numarası Örnek: 905555555555 >>> ")

mesaj = input("Mesajınız >>> ")

arlk = mesaj[0:70]

print("\n| Mesajınızın Gönderilebilecek Kısmı Aşagıdaki Gibidir.\n"+arlk)

drlm = input("\n| Mesajınız Gönderilsinmi?[y/n] >>> ")

if drlm == "y" or drlm == "Y":
    print("\n"+sor+"\n"+arlk+"\n")
    resp = requests.post('https://textbelt.com/text', {
  'phone': sor,
  'message': arlk,
  'key': 'textbelt',
    })
    print(resp.json())

elif drlm == "n" or drlm == "N":
    quit()
else:
    print("\n|Hata Tespit Edildi!")
