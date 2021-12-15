""" 
(x,y) şeklinde verilen bir üçgende sonradan verilen (x,y) 
ikililerin alanın içinde olup olmadığını kontrol eden program.
Örnek: üçgen --> (0,0)(0,5)(7,0) aranan nokta (0.2)
"""

(a1,b1)=(0,0)

(a2,b2)=(0,5)

(a3,b3)=(7,0)

(x,y)=(0,2)

Ucgen_Alan=1/2*abs((a1*b2+a2*b3+a3*b1)-(a2*b1+a3*b2+a1*b3))

A1=1/2*abs((a1*b2+a2*y+x*b1)-(a2*b1+x*b2+a1*y))
A2=1/2*abs((a1*y+x*b3+a3*b1)-(x*b1+a3*y+a1*b3))
A3=1/2*abs((x*b2+a2*b3+a3*y)-(a2*y+a3*b2+x*b3))

if A1+A2+A3 == Ucgen_Alan :
    print("Bu bir üçgendir")