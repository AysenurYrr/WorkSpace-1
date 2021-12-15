

x=int(input("Bir sayi giriniz:"))
def faktoryel(x):
    carpim=1
    i=1
    while i<=x:
        carpim*=i
        i+=1
    return(carpim)

print(faktoryel(x))