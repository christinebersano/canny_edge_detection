import cv2

cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Error: Unable to access the camera.")
    exit()

while True:
   
    ret, frame = cap.read()

    
    if not ret:
        print("Error: Could not retrieve a frame from the camera.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold1=100, threshold2=200)

    cv2.imshow('Input Frame', frame)
    cv2.imshow('Canny Edge Detection Output', edges)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break


cap.release()
cv2.destroyAllWindows()