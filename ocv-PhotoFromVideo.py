import cv2

cap = cv2.VideoCapture(0)

muestra = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()


    #Capture Frame
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("muestra" +str(muestra) +".png", frame)
        print("Muestra" +str(muestra) +" Saved")
        muestra = muestra + 1


    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()