import cv2

img = cv2.imread("./sample.jpg", 1)
start_x, start_y, end_x, end_y = 0, 0, 0, 0

def drawRectangle(action, x, y, flags, userdata):
    global start_x, start_y, end_x, end_y, img
    if action == cv2.EVENT_LBUTTONDOWN:
        start_x = x
        start_y = y
        img = cv2.imread("./sample.jpg", 1) 
        cv2.circle(img, (start_x, start_y), radius=0, color=(255, 255, 0) , thickness=-2)
        
    elif action == cv2.EVENT_LBUTTONUP:
        end_x = x
        end_y = y
        cv2.rectangle(img, (start_x, start_y), (end_x, end_y), color=(255, 255, 0), thickness=2)
        cv2.imshow("Window", img)

dummy = img.copy()
cv2.namedWindow("Window")
cv2.setMouseCallback("Window", drawRectangle)

k = 0 
while k!=27:
    cv2.imshow("Window", img)
    cv2.putText(img, '''Choose top left corner, and drag, ?''', 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                 0.7, (255, 255, 255), 2)

    k = cv2.waitKey(1) & 0xFF
    if k == 99:
        img = dummy.copy()

    crop = img[start_y: end_y, start_x: end_x]
    if len(crop) > 0:
        cv2.imwrite("./face.png", crop)    

cv2.destroyAllWindows()
