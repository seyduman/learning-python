
#şeyma duman- basit python kodlama 


# print("hello world") #ekrana yazı yazdırma

# isim= input("lütfen adınızı giriniz")
# print("merhaba" +isim + "hoşgeldiniz") #input kullanımı/ kullanıcı ismini alma

#iiki sayının ortalaması 

# sayi1= input ('birinci sayıyı giriniz')
# sayi2=input ('ikinci sayıyı giriniz')
# ort=(int(sayi1)+int(sayi2))/2
# print("sayıların ortalaması : {0}" .format(ort))

#iki sayının toplamı

# sayi1= input ('ilk sayiyi giriniz')
# sayi2= input ('ikinci sayıyı giriniz')
# top=(int(sayi1)+int(sayi2))
# print("sayilar toplami {0}".format(top))

#vize final not ortalaması hesaplama

# vize=input ('vize notunuzu giriniz:')
# final=input ('final notunuzu giriniz:')
# ortalama =(float(vize)*0.4)+(float(final)*0.6)
# print("sınavlarınızın ortalaması:{0}".format(ortalama))
#////////////////////////////////////////////////////////

#if-else kullanımı
#sayı tek mi cift mi

# sayi1= input ('sayiyi giriniz')
# if (int(sayi1)%2==0):
#     print("sayı cifttir")
# else:
#     print("sayı tektir")

#sayı negatif mi pozitif mi
# sayi1= input ('sayiyi giriniz')
# if (int(sayi1)>0):
#     print("sayı pozitiftir")
# elif (int(sayi1)<0):
#     print("sayı negatiftir")
# else:
#     print("sayı sıfırdır")

#ehliyet alabiliyor mu
# yas= input('yaşınıızı giriniz:')
# if(int (yas)>=18):
#     print("ehliyet alabilir")
# else:
#     print("ehliyet alamaz")

#sınıf geçme
# ort=input("ortalamanızı giriniz:")
# if(int(ort)<60):
#     print("sınıfta kaldınız")
# else:
#     print("sınıfı geçtiniz")
#////////////////////////////////////////////////////////

#donguler-listeleme
# for i in range(1,101):
#     print (i)

# for i in range(1,101):
#     if(i%2==0):
#         print(i)

# for i in range(1,101):
#     if(i%2!=0):
#         print(i)

# for i in range(1,101):
#     if(i%3==0 and i%5==0): #aynı sekilde or ile de kullanılabili
#         print(i)

# sayi= input('bir sayı giriniz')
# for i in range(1,int(sayi)+1):
#     print(i)
#////////////////////////////////////////////////////////
#dikdortgenin alanı cevresi hesaplama

# kisakenar=input('kısa kenar degeri giriniz:')
# uzunkenar=input('uzun kenar degeri giriniz:')
# alan=(int(kisakenar)*int(uzunkenar))
# print("alan : {0}".format(alan))
# cevre=2*(int(kisakenar)+int(uzunkenar))
# print("cevre: {0}".format(cevre))

# isim=input("Adınızı Girin ")
# sayac=0
# while sayac < len(isim):
#     print(isim[sayac])
#     sayac += 1
# else:
#     print("Adının harflerini listeledim.")

#Kullanıcın girdiği iki sayı arasındaki sayıların toplamı

# toplam=0
# sayi1=input('1. Sayı: ')
# sayi2=input('2. Sayı: ')
# for i in range(int(sayi1)+1,int(sayi2)):
#       toplam+=i
# print("{0} ile {1} arasındaki sayıların toplamı : {2}".format(sayi1,sayi2,toplam))

#girilen sayı asal mı degil mi
sayac=0
sayi=input('Sayı: ')
for i in range(2,int(sayi)):
      if(int(sayi)%i==0):
            sayac+=1
            break
if(sayac!=0):
      print("Sayı Asal Değil")
else:
      print("Sayı Asal")

#1 den kullanıcının girmiş olduğu sayıya kadar olan tek ve çift sayıların toplamını ayrı ayrı bulan
sayi = input('Sayıyı Girin : ')
tekToplam=0
ciftToplam=0
for i in range(1,int(sayi)):
      if(i%2==0):
            ciftToplam+=i
      else:
            tekToplam+=i
print("Tek Sayıların Toplamı : {0}".format(tekToplam))
print("Çift Sayıların Toplamı : {0}".format(ciftToplam))

#Maaşı ve zam oranı girilen işçinin zamlı maaşını hesapla
yeniMaas=0
maas=input("Maaşı Gir : ")
zam=input("Zam Oranı(%) : ")
yeniMaas=int(maas)+(int(maas)*int(zam)/100)
print("Zamlı Maaş :",yeniMaas)
