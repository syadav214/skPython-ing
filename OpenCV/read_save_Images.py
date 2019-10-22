import cv2

image = cv2.imread('Good.jpg',1)
# 1=> color, 0=> grey scale

print(image.shape)

image = cv2.resize(image, (500,500))

cv2.imshow('image',image)

k = cv2.waitKey(0) # it waits for any key to be pressed to execute next step

if k == 27: # wait for ESC key to exit
  
    cv2.destroyAllWindows()
    
elif k == ord('s'): # wait for 's' key to save and exit
  
    cv2.imwrite('watchgray.png',image)
    
    cv2.destroyAllWindows()

