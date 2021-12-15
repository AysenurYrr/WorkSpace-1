import cv2
img=cv2.imread("resim.jpg")
x=0
y=0

xlenaxis=1216
ylenaxis=1600
x_total=0
xy_counter=0
y_total=0

while True:
    if img.item(x,y,2) != 255 :
        print(x,y)
        x_total+=x
        y_total+=y
        xy_counter+=1

    y+=1
    if y==ylenaxis:
        x+=1
        y=0
        if x==xlenaxis:
            break

x_mid=x_total/xy_counter
y_mid=y_total/xy_counter
print("Orta nokta x,y:",x_mid,y_mid)

while(1):
    cv2.imshow("paint",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows

