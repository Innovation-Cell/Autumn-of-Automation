import cv2

img = cv2.imread('lena.jpg', 0)
cv2.imshow('Lena', img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite('ekaurLena.png', img)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()

live_vid = cv2.VideoCapture(0)

#in order to save your Awesome video just uncomment the "#'s"

#fourcc = cv2.VideoWriter_fourcc(*"XVID")
#sav_video = cv2.VideoWriter("Myvideo.avi", fourcc, 20.0, (640, 480)) #u can use any size instead of (640, 480)

while(live_vid.isOpened()):
    truth, frame = live_vid.read()
    if truth:
        #sav_video.write(frame)

        r2b = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        cv2.imshow('video', r2b)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
live_vid.release()
#sav_video.release()
cv2.destroyAllWindows()

