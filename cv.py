import cv2
vid = cv2.VideoCapture(0)
while True:
    ret, frame = vid.read()
    image = cv2.putText(frame,'Welcome to AI ML class',(50,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,250),4,cv2.LINE_AA)
    cv2.imshow('AI-VIDEO',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()