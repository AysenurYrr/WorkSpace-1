
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", 12345))

f = open("/home/ayeneko/Documents/Python/resim.jpg", "rb")
data = f.read()

while data:
    s.send(data)
    data = f.read()

f.close()
print("Dosya gönderildi.")