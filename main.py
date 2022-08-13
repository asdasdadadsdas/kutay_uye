# encoding utf-8

from time import sleep
from pyrogram import Client

from pyrogram.errors import FloodWait
from pyrogram.errors import AuthKeyDuplicated
from pyrogram.errors import UserNotMutualContact
from pyrogram.errors import UserPrivacyRestricted
from pyrogram.errors import ChatAdminRequired
from pyrogram.errors import PeerFlood
from pyrogram.errors import FloodWait
from pyrogram.errors import UserKicked
from pyrogram.errors import UserChannelsTooMuch
from pyrogram.errors import UserDeactivated
from pyrogram.errors import UserDeactivatedBan


api_id = 1796707
api_hash = "f0a0c6671b2710716145c086576a4640"



ekle = input("\n\nHesap ekleyecek misiniz(daha önce ekledikleriniz duruyor !) ? \n(E/H)->  ")
if ekle == "E" or "e" or "evet" or "Evet":
    sayi = int(input("Kaç Hesap Eklemek İstiyorsunuz: \n->  "))
    for i in range(sayi):
        numara = input("Numara giriniz:(ülke kodu dahil. Örn: +90651*****)  :   ")
        print("Gelen Kodu Giriniz: ")
        with Client(":memory:", api_id, api_hash, phone_number=numara) as ses:
            session = ses.export_session_string()
            with open("hesaplar.txt", "a+", encoding="utf-8") as dosya:
                dosya.write("\n" + session)
                print("Eklendi...\n\n")
else:
    pass




# Clientlerin Başlatılması
hesaplar = []
sayac_client = 1
with open("hesaplar.txt","r",encoding="utf-8") as dosya:
    for session in dosya:
        if sayac_client == 1:
            app1 = Client(session, api_id, api_hash, plugins=dict(""))
            hesaplar.append(app1)
        if sayac_client == 2:
            app2 = Client(session, api_id, api_hash, plugins=dict(""))
            hesaplar.append(app2)
        if sayac_client == 3:
            app3 = Client(session, api_id, api_hash, plugins=dict(""))
            hesaplar.append(app3)
        if sayac_client == 4:
            app4 = Client(session, api_id, api_hash, plugins=dict(""))
            hesaplar.append(app4)
        if sayac_client == 5:
            app5 = Client(session, api_id, api_hash, plugins=dict(""))
            hesaplar.append(app5)
        if sayac_client == 6:
            app6 = Client(session, api_id, api_hash, plugins=dict(""))
            hesaplar.append(app6)
        if sayac_client == 7:
            app7 = Client(session, api_id, api_hash, plugins=dict(""))
            hesaplar.append(app7)
        if sayac_client == 8:
            app8 = Client(session, api_id, api_hash, plugins=dict(""))
            hesaplar.append(app8)
        if sayac_client == 9:
            app9 = Client(session, api_id, api_hash, plugins=dict(""))
            hesaplar.append(app9)
        if sayac_client == 10:
            app10 = Client(session, api_id, api_hash, plugins=dict(""))
            hesaplar.append(app10)
        if sayac_client == 11:
            app11 = Client(session, api_id, api_hash, plugins=dict(""))
            hesaplar.append(app11)
        if sayac_client == 12:
            app12 = Client(session, api_id, api_hash, plugins=dict(""))
            hesaplar.append(app12)
        sayac_client+=1

sayac_client = 1
for hesap in hesaplar:
    try:
        hesap.start()
        print(f"{sayac_client}. Hesap Başlatıldı.")
    except:
        print(f"!!!!!!! {sayac_client} ARIZALI !!!!!!!")
    sayac_client +=1
print("Hesaplar Başarıyla Başlatıldı\n-----------------------")

eklenecek = str(input("\n\n\nEklenecek grup linki:\n> ")).replace("https://t.me/","")
cekilecek = str(input("\n\n\nÇekilecek grup linki:\n> ")).replace("https://t.me/","")
print("\n\nEkleme İşlemi Başladı ! \n")
sayi = 0   
while True:
    for hesap in hesaplar:
        try:
            eklenecek_chat = eklenecek
            hesap.join_chat(eklenecek_chat)
            secilen = cekilecek
            users = hesap.iter_chat_members(secilen, limit=100)
        except:
            users = []

        for user in users:
            if not user.user.is_bot or not user.user.is_deleted:
                try:
                    hesap.add_chat_members(eklenecek_chat,user.user.id)
                    sayi += 1
                        
                except UserNotMutualContact:
                    pass
                except UserPrivacyRestricted:
                    pass
                except ChatAdminRequired:
                    pass
                except KeyError:
                    pass
                except UserKicked:
                    pass
                except UserChannelsTooMuch:
                    pass
                except FloodWait as FW:
                    print(f"{FW.x} Saniye Spam.")
                    break
                except PeerFlood:
                    print(PeerFlood)
                    break
                except:
                    pass

                print(str(sayi) + " - " + secilen + "  -  " + user.user.first_name)
                sleep(3)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

