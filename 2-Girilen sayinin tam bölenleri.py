
""" Girilen sayının bütün bölenlerini bulan kod"""

x=int(input("Bir sayi giriniz."))
a=1
liste=list()
while (x>a):
    if x%a==0:
        liste.append([a])
        print(str(len(liste))+". bölen",a,"dir.")
    a+=1
