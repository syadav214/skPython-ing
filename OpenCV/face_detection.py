import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
image = cv2.imread('paulwalker1.jpg',1)

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.05, minNeighbors = 5)

# Let us print the no. of faces found
print('Faces found: ', len(faces))
print(type(faces))
print(faces)


for (x,y,w,h) in faces:
     cv2.rectangle(gray_image, (x, y), (x+w, y+h), (0, 255, 0), 3)

image = cv2.resize(gray_image, (500,500))

cv2.imshow('image',image)

cv2.waitKey(0) 
cv2.destroyAllWindows()
