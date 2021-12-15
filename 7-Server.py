"""
İki terminal arasında resim gönder. 
Resim boyutu en az 100kb olmalıdır.
"""
#!/usr/bin/env python3
#server dosyasi

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 12345))
s.listen(10)


print("Sunucu açıldı...\nİstemciler bekleniyor...")

while True:
    c, addr = s.accept()
    print('\n{} bağlandı.'.format(addr))
    datas = c.recv(1024)
    f = open("dosya.jpg", "wb")
    while datas:
        f.write(datas)
        datas = c.recv(1024)
    f.close()
    print("resim alındı...")
    continue