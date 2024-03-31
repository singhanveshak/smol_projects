'''
ANVESHAK SINGH, 19 March 2024. Assignment by R. Louis Sir

How to run program ?

$> python answers.py <path to fits file>

Example:
$> python answers.py 
'''

from astropy.io import fits
import numpy as np
import cv2
import sys

hdul = fits.open(sys.argv[1])                                           # open file
uint16 = hdul[0].data                                                   # capture 2048*2048 matrix (type = unsigned 16)
hdul.close()                                                            # close file

############################################################################################################3
# QUESTION 1 

uint8 = cv2.convertScaleAbs(uint16, alpha=(255.0/65535.0))              # from uint16 to uint8 since cv2.HoughCircles() only works with uint8
uint8[uint8 > 10] = 255                                                 # Apply the imdat > 10 to set values above 10 to 1 and rest to 0
uint8[~uint8 > 10] = 0

detected_circles = cv2.HoughCircles(uint8,  method=cv2.HOUGH_GRADIENT, dp=1, minDist=100, param1 = 100, param2 = 10, minRadius =700, maxRadius = 800) 
if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles)) 

    circleList = []                                                     # to store centres, radii of possible circle
    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 
        cv2.circle(uint8, (a, b), r, (255, 0, 0), 2)                    # draw circumference
        cv2.circle(uint8, (a, b), 2, (0, 0, 255), 3)                    # draw small circle for radius
        cv2.putText(uint8, f' {(a,b)}, r={r}', (a,b), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 1)
        circleList.append((a,b,r))

    cv2.imshow('POSSIBLE SUN CENTERS (Please scroll through image to show whole surface)', uint8) 
    cv2.waitKey(0)

if(len(circleList) > 0):
    print('\nPOSSIBLE CENTERS AND RADII...')
    for _ in circleList:
        print(f'SUN CENTER = {_[0:2]}, SUN RADIUS = {_[2]}')

    # save ANSWER 1 as png
    cv2.imwrite('ANSWER1.png', uint8) 
else:
    print('NO CIRCLE DETECTED')


#############################################################################################################
# QUESTION 2
    
uint8 = cv2.convertScaleAbs(uint16, alpha=(255.0/65535.0))              # from uint16 to uint8 since cv2.adaptiveThreshold() only works with uint8
uint8[uint8 <= 10] = 0                                                  # to blacken the sun background, make thresholding easier :)
image_blur = cv2.GaussianBlur(uint8, (5,5), 0)       
binary_img = cv2.adaptiveThreshold(image_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 9, 3)
cv2.imshow("POSSIBLE SUNSPOTS (Please scroll through image to show whole surface)",binary_img)
cv2.waitKey(0)

# Save ANSWER 2 in text format
np.savetxt('ANSWER2a.txt', binary_img, delimiter=' ',fmt='%d')

#  Save ANSWER 2 in fits file 
hdu = fits.PrimaryHDU(binary_img)
hdul = fits.HDUList([hdu])
hdul.writeto('ANSWER2.fits', overwrite=True)

#  Save ANSWER 2 as png 
cv2.destroyAllWindows()
cv2.imwrite('ANSWER2.png', binary_img) 
 

#############################################################################################################

print('\nANSWERS SAVED:\tANSWER1.png\tANSWER2.txt, ANSWER2.fits, ANSWER2.png')
