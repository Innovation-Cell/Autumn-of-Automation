import cv2

live_vid = cv2.VideoCapture(0)


while(live_vid.isOpened()):
    truth, frame = live_vid.read()
    if truth:
        canny_vid = cv2.Canny(frame, 100, 200)
        cv2.imshow('video', canny_vid)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
live_vid.release()
cv2.destroyAllWindows()