from methods import *
import os

aciklama="""
1-) Ağ Id Belirle
2-) Broadcast Adresi Belirle
3-) CIDR > Classic : Classic > CIDR 
4-) Alt Ağ oluştur
"""

if os.name=="nt":
    oss="cls"
if os.name=="posix":
    oss="clear"

while True:
    while True:
        print(aciklama)
        secenek = input("İşlem Seçin => ")
        if secenek != "1" and secenek != "2" and secenek != "3" and secenek != "4":
            os.system(oss)
            print("Hatalı Giriş !!")
        else:
            break

    if secenek == "1":
        while True:
            print("#"*50)
            try:
                ip = input("İp Adresi Girin :")
                ip = [ int(ip.split(".")[0]) , int(ip.split(".")[1]) , int(ip.split(".")[2]) , int(ip.split(".")[3]) ]
                sm = input("Subnet Mask Girin :")
                sm = [ int(sm.split(".")[0]) , int(sm.split(".")[1]) , int(sm.split(".")[2]) , int(sm.split(".")[3]) ]
                if octetAuth(ip) and octetAuth(sm):
                    break
                else :
                    print("Değerler 0-255 arası olmalı!")
                    continue
            except:
                print("Hatalı Giriş")
                input()

        sonuc=[]
        for i in netId(ip,sm):
            sonuc.append(str(i))
        print("Network ID : ",(".".join(sonuc)))
        print("#"*50)
        input()
        os.system(oss)

    if secenek == "2":
        while True:
            print("#"*50)
            try:
                ip = input("İp Adresi Girin :")
                ip = [ int(ip.split(".")[0]) , int(ip.split(".")[1]) , int(ip.split(".")[2]) , int(ip.split(".")[3])]
                sm = input("Subnet Mask Girin :")
                sm = [ int(sm.split(".")[0]) , int(sm.split(".")[1]) , int(sm.split(".")[2]) , int(sm.split(".")[3])]
                if octetAuth(ip) and octetAuth(sm):
                   break
                else :
                   print("Değerler 0-255 arası olmalı!")
                   continue
            except:
                print("Hatali Giriş!")
                input()

        bradcast =[] 
        for i in broadcast(ip,sm):
            bradcast.append(str(i))
        print("Broadcast Adresi :",".".join(bradcast))
        print("#"*50)
        input()
        os.system(oss)

    if secenek == "3":
        while True:
            print("#"*50)
            try:
                sm = input("Subnet Mask Girin (xx.xx.xx.xx),/xx:")
                if len(sm) <= 2:
                    if int(sm)<0 or int(sm)>32:
                        print("CIDR değeri Hatalı")
                        continue
                    print("Standat Subnet Mask : ",".".join([str(item) for item in cidrtoclassic(sm)])) 
                elif len(sm) > 2:
                    sm = [int(sm.split(".")[0]),int(sm.split(".")[1]),int(sm.split(".")[2]),int(sm.split(".")[3])]
                    if octetAuth(sm):
                        print("CIDR Subnet Mask : ",stdToCidr(sm))
                        break
                    else :
                        print("Değerler 0-255 arası olmalı!")
                        continue
                else:
                    print("Hatalı Giriş")
                break
            except:
                print("Hatalı Giriş")
        print("#"*50)
        input()
        os.system(oss)

    if secenek == "4":
        while True:
            print("#"*50)
            ip = input("İp Adresi Girin : ")
            ip = [int(ip.split(".")[0]),int(ip.split(".")[1]),int(ip.split(".")[2]),int(ip.split(".")[3])]
            sm = input("Subnet Mask Girin : ")
            if len(sm) > 2:
                sm = [int(sm.split(".")[0]),int(sm.split(".")[1]),int(sm.split(".")[2]),int(sm.split(".")[3])] 
            else:
                sm = cidrtoclassic(sm) # int Tipinde ağ maskesi
            if octetAuth(ip) and octetAuth(sm):
               break
            else :
               print("Değerler 0-255 arası olmalı!")
               continue
        bolunenAgSayisi = input("Kaç Adet Ağ Oluşturulacak :")
        print("#"*50)
        netCreator(bolunenAgSayisi,ip,sm)
        print("#"*50)
        