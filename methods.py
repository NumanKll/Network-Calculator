# Ağ Adresinin integer tipinde oktetlerini binary olarak verir 
def intToBin(oktet): # İnteger sayısal değer alır
    rtrn = ""
    if 8 != len(bin(oktet)[2:]):
        for c in range(8-len(bin(oktet)[2:])):
            rtrn = rtrn+"0"
        return rtrn + bin(oktet)[2:] # 8 Bit Sring Değer döner
    else:
        return bin(oktet)[2:] # 8 Bit Sring Değer döner

# Standart subnet değerini CIDR değerine dönüştürür
def stdToCidr(ls):
    clas = ""
    for i in ls:
        clas = clas + bin(i)[2:]
    return len(clas.replace("0","")) # İnt Tipinde Sayı döner

# Binary tipinde verilen 8 bit karakter dizilerini integer değere çevirir
def binToInt(oktet): # 8 Bit String Değer alır
    dec=0
    oktet=oktet[::-1]
    for i in range(0,8):
        dec = dec + int(oktet[i])*(2**i)
    return dec # İnteger Değer Döner

# Ip adresi ve Subnet ile Ağ Id değerini hesaplar
def netId(ip,sub): # İnteger Tipinde 4 Oktetli Liste Alır
    netId=[]
    for a in range(4):
        oktet=""
        for i,s in zip(intToBin(ip[a]),intToBin(sub[a])):
            oktet = oktet + (str(int(i) and int(s)))
        netId.append(binToInt(oktet))
    return netId # Integer Tipinde 4 Oktetli Değer Döndürür 

# Ağa Ait Broadcast Adresini Hesaplar
def broadcast(ip,sub): # Broadcast adresini İnteger olarak verir
    iplen=""
    sublen=""
    for x in range(4):
        iplen = iplen + str(intToBin(ip[x]))
    for z in range(4):
        sublen = sublen + str(intToBin(sub[z]))
    for c,s in enumerate(sublen):
        if s == "0":
            iplen = iplen[:c] + "1" + iplen[c + 1:]
    return [binToInt(iplen[:8]),binToInt(iplen[8:16]),binToInt(iplen[16:24]),binToInt(iplen[24:32])] # Integer Tipinde 4 Oktetli Liste Döndürür

# Bölünecek Alt ağ sayısına göre Subnet adresine eklenecek Bit Sayısını Hesaplar
def subnetNumber(netnumber): # Integer Tipinde Değer Alır
    for i in range(32):
        if int(netnumber) <= (2**i):
            netnumber = i 
            break 
    return netnumber # İnteger Tipinde Değer Döndürür

# Yeni Subneti Hesaplar
def subnetCalculator(newSubnetbit,sub): # Yeni subnete eklenecek bit sayısını ve eski subneti liste şeklinde alır
    subBin=intToBin(sub[0])+intToBin(sub[1])+intToBin(sub[2])+intToBin(sub[3])
    subBin = subBin.replace("0","")
    for i in range(newSubnetbit):
        subBin=subBin + "1"
    if len(subBin)<32:
        for c in range(32-len(subBin)):
            subBin=subBin + "0"
    return [binToInt(subBin[:8]),binToInt(subBin[8:16]),binToInt(subBin[16:24]),binToInt(subBin[24:32])] # 4 Oktetli Liste tipinde integer deger döndürür

# Yeni subnette kalan geçerli oktetteki sıfır sayısını hesaplar
def subnetZeroNumber(netId,sub):
    for z in range(0,4):
        if netId[z] == 0:
            oktet=z
            zeroCount=0
            for i,s in zip(intToBin(netId[z]),intToBin(sub[z])):
                if s == "0":
                    zeroCount+=1
            break
    return zeroCount,oktet

# Standart Subneti CIDR 
def cidrtoclassic(olen):
    cls=""
    ip=[]
    if len(olen) <= 2:
        for i in range(int(olen)):
            cls = cls + "1"
        if len(cls) < 32:
            a = 32 - len(cls)
        for a in range(a):
            cls = cls + "0"
        ip.append(binToInt(cls[:8]))
        ip.append(binToInt(cls[8:16]))
        ip.append(binToInt(cls[16:24]))
        ip.append(binToInt(cls[24:32]))
    return ip

# Ağ ID değerin
def startIp(ip):
    ip[3]=ip[3]+1
    return ip

# Girilen İp octetlerini uygun değerlerde olup olmadığını kontrol eder
def octetAuth(octet):
    rtrn = True
    for i in octet:
        if i<0 or i>255:
            rtrn = False
    return rtrn

# Yeni Alt Ağları ve Bilgileri Listeler
def netCreator(bolunenAgSayisi,ip,sm):

    netBit = subnetNumber(bolunenAgSayisi) # (2**netbit) Bölünen Ağ Sayısını verir
    
    newSubnet = subnetCalculator(netBit,sm)
    
    netid = netId(ip,newSubnet)
    hostbit,octet= subnetZeroNumber(netid,newSubnet)

    if octet==3:
        hostCount=(2**hostbit)-2
    elif octet==2:
        hostCount=(2**hostbit*2**8)-2
    elif octet==1:
        hostCount=(2**hostbit*(2*2**8))-2

    for i in range(2**netBit):
        print(f"#### Ağ {i} ######")
        print("Subnet Mask      :",('.'.join([str(item) for item in newSubnet])))
        print("Network ID       :",('.'.join([str(item) for item in netid])))
        print("Ağ Aralığı       :",('.'.join([str(item) for item in startIp(netid)])),end="-")
        endIP=broadcast(netid,newSubnet)
        endIP[3]=endIP[3]-1
        print(('.'.join([str(item) for item in endIP])))
        print("Host Sayısı      :",hostCount)
        netid[octet] = 2**hostbit*(i+1)
        print("Broadcast Adresi :",('.'.join([str(item) for item in broadcast(netid,newSubnet)])))
        print("----------------------------------")
