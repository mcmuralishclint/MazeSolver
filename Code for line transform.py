import numpy as np
import cv2
import matplotlib
from PIL import Image
import os.path
            
i = Image.open('new4.jpg')               #open the image
height,width=i.size                      #find the image dimensions
iar = np.array(i)                       #creating an array
blank=np.zeros((1500,1500,3),np.uint8)  #create a blank enviromnent for sketching
blank.fill(255);
i=0                                     #row count
j=0                                     #column count

for i in range(width-1):                   #As long as the count is within row bounds
        for j in range(height-1):           #As long as the count is within column bounds
            a,b,c=(iar[i,j])            #Setting the BGR values of the pixel
            if (a<100):                 #If a black pixel is detected
                blank=cv2.line(blank,(i+5,j+5),(i+6,j+6),(0,0,0),1)  #plot the pixel
                          
cv2.imwrite('beforeRotation.jpg',blank) #Save the image
img=cv2.imread('beforeRotation.jpg',0)  #Read the saved image as grayscale
rows,cols=img.shape                     #Get the Black and white pixel values
M = cv2.getRotationMatrix2D((cols/2,rows/2),270,1) #Rotate by 270 degrees
dst = cv2.warpAffine(img,M,(cols,rows)) #Format the image to actual size       
cv2.imwrite('After Rotation.jpg',dst)   #Save the rotated image
im = np.fliplr((cv2.imread('After Rotation.jpg',0))) #Reflect the image by y axis  
cv2.imwrite('After Reflection.jpg',im)  #Save the final image
print('Done')                           #Display a success message


