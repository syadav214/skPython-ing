import cv2,time

video = cv2.VideoCapture(0) # it will capture via your default webcam

check, frame = video.read()

print(check)
#print(frame)

cv2.imshow('test',frame)
cv2.waitkey(0)

time.sleep(3)

video.release()

cv2.destroyAllWindows()
