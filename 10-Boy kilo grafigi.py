

import matplotlib.pyplot as plt
 
# Boy
x = [150,160,155,170,165,190,157,173,179,163]
# Kilo
y = [50,60,55,49,65,90,40,85,69,100]
 
plt.scatter(x, y, label= "circle", color= "red",
            marker= "o")
 

plt.xlabel('Boy (metre)')

plt.ylabel('Kilo (kilogram)')

plt.title('10 Ogrenciye ait boy kilo grafigi')

plt.legend()
 
plt.show()