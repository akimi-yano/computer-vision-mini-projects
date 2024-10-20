import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

im = np.zeros((10,10),dtype='uint8')
print(im)
plt.imshow(im)

im[0,1] = 1
im[-1,0]= 1
im[-2,-1]=1
im[2,2] = 1
im[5:8,5:8] = 1

print(im)
plt.imshow(im)

element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
print(element)

ksize = element.shape[0]
height,width = im.shape[:2]
print(ksize)
print(ksize//2)

border = ksize//2
paddedIm = np.zeros((height + border*2, width + border*2))
paddedIm = cv2.copyMakeBorder(im, border, border, border, border, cv2.BORDER_CONSTANT, value = 0)
paddedDilatedIm = paddedIm.copy()

# Use frame size as 50x50
out = cv2.VideoWriter("dilationScratch.avi", cv2.VideoWriter_fourcc('M','J','P','G'), 10, (50, 50))

for h_i in range(border, height+border):
    for w_i in range(border,width+border):
        neighborhood = paddedIm[ h_i - border : (h_i + border)+1, w_i - border : (w_i + border)+1]
        and_operation = cv2.bitwise_and(neighborhood, element)
        max_val = np.max(and_operation)
        
        if max_val > 0:
            paddedDilatedIm[h_i, w_i] = max_val

        # Resize output to 50x50 before writing it to the video
        dilatedImage = paddedDilatedIm[border:border+height,border:border+width]
        resizedFrame = cv2.resize(dilatedImage, (50, 50), interpolation=cv2.INTER_NEAREST)
        resizedFrame *= 255  
        resizedFrame = np.clip(resizedFrame, 0, 255).astype(np.uint8)
        # Convert resizedFrame to BGR before writing
        resizedFrameBGR = cv2.cvtColor(resizedFrame, cv2.COLOR_GRAY2BGR)
        out.write(resizedFrameBGR)

# Release the VideoWriter object
out.release()