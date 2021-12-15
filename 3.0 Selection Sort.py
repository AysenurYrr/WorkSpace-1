
#Selection Sort


liste= [5,33,12,1,56]
yeni_liste = []
sayac=0

while sayac<len(liste):
    i=liste[0]
    for j in range(0,len(liste)):
        if liste[j] < i:
            i = liste[j]
    print(i)
    liste.remove(i)
    yeni_liste.append(i)
print(yeni_liste)