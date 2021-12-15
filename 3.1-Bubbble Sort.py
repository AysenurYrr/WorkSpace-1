
#Bubble Sort

liste= [5,33,12,1,56]
print(liste)
x=0
a=len(liste)
while a >=1 :
    if x+1 == len(liste):
        x=0
        a-=1
    if liste[x]>liste[x+1]:
        liste[x],liste[x+1]=liste[x+1],liste[x]
    x+=1
print(liste)
    