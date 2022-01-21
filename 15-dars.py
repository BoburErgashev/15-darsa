# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 21:49:42 2022

@author: Bobur
"""
talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
      }
izohli_lugat={
    "boolean":"mantiqiy qiymat",
    "float":"o\'nlik son",
    "for":"biror narsani qayta qayta bajarish sikli",
    "If":"shartlarni tekshirish",
    "Integer":"butun son",
    "len":"qatorni aniqlash",
    "toople":"o\'zgarmas royhat",
    "title":"so\'zni bosh harfini kattada boshlaydi",
    "little":"so\'zdagi hamma harflarni kichkina qiladi",
    "upper":"so\'zlarni kotta harfga aylantiradi",
    "range":"sonlarni ketmaketligini to\'g\'irlaydi"
    }
print("Pythin elementlar ro'yxati:")
for k,v in sorted(izohli_lugat.items()):
    print(f"{k.title()}-{v}")
davlatlar={
    "avg\'oniston":"kobul",
    "qozog\'iston":"nursultan",
    "qirg\'iziston":"kesh",
    "o\'zbeksistn":"toshkent",
    "aqsh":"vashington",
    "buyuk britanya":"london"}
for key in sorted(davlatlar.keys()):
    print(key.upper())
for value in sorted(davlatlar.values()):
    print(value.title())
country=input("Qaysi davlat haqida bilishni hohlaysiz?\n Istalgan davlatni kiriting>>>")
capital=davlatlar.get(country)
if capital==None:
    print("Bizda bunday malumot yo\'q")
else:
    print(f"{country.upper()} davlatining poytaxti {capital.upper()} shaxrti!!!")
menu={
      "somsa go\'shtli":3000,
      "soms tovuqli":2500,
      "ko\'k somsa":7000,
      "lag\'mon":5000,
      "chuchvara":90000,
      "kartoshka pyure":100000,
      "tovuq go\'sht":2000}
print("3 taom buyurtnma qiling.")
buyurtmalar=[]
for n in range(3):
    buyurtmalar.append(input(f"{n+1}- taom:").lower())
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so\'m")
    else:
         print(f"Kechirasiz bizda {buyurtma} yo\'q ")
    
    
    
    
    
    
    
    