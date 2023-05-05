import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(20,300), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.putText(img,"Mercury",(110,265), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Venus",(190,270), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Earth",(290,270), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Mars",(379,259), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Jupiter",(570,300), cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255))
cv2.putText(img,"Saturn",(750,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Uranus",(970,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Neptune",(1100,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imwrite("Solar_system_with_name.jpg",img)
cv2.imshow("output", img)
cv2.waitKey(0)

