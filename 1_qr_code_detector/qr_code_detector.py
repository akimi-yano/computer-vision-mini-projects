import cv2
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['figure.figsize'] = (10.0, 10.0)
imgPath = "./IDCard-Satya.png"
img = cv2.imread(imgPath, cv2.IMREAD_COLOR)

qrDecoder = cv2.QRCodeDetector()
opencvData, bbox, rectifiedImage = qrDecoder.detectAndDecode(img)

if opencvData != None:
    print("QR Code Detected")
else:
    print("QR Code NOT Detected")

n = len(bbox)

for i in range(n):
    # The cv2.line() function is used to draw a straight line between two points in the image (img).
    start_of_line = tuple(bbox[i][0])
    start_of_line = tuple(map(int, start_of_line)) 
    # The mod % below ensures that the lines connect all corners in sequence, and the last line closes the loop.
    end_of_line = tuple(bbox[(i+1) % len(bbox)][0])
    end_of_line = tuple(map(int, end_of_line)) 
    cv2.line(img, start_of_line,end_of_line, color=(255, 0, 0), thickness=2)
    
# Since we have already detected and decoded the QR Code
# using qrDecoder.detectAndDecode, we will directly
# use the decoded text we obtained at that step (opencvdata)

print("QR Code Detected!")
print(opencvData)

resultImagePath = "QRCode-Output.png"
cv2.imwrite(resultImagePath, rectifiedImage)

# OpenCV uses BGR whereas Matplotlib uses RGB format
# So convert the BGR image to RGB image
# And display the correct image
plt.imshow(img[:,:,::-1])
plt.show()