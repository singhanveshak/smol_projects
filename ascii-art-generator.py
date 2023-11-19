'''
Author: Anveshak Singh @singhanveshak
Date: 19/11/2023
This script reads in an image-> converts it to a numpy array-> substitutes groups of pixels with ascii symbols
ascii-greyscale: " .:-=+*#%@" (lighter to darker brightness)
'''
from PIL import Image
import numpy as np
from sys import argv

filename=argv[1]
im=np.array(Image.open(filename).convert("L"))
n_rows, n_cols=im.shape[0],im.shape[1]
gs=" .:-=+*#%@"
l_gs=len(gs)
s=int(input("Enter the scale by which to reduce image size? "))                             #image is diminished by this scale
s_row,s_col=2*s,s                            

#resize image according to scale s
if(n_rows%s_row!=0):
    im=np.delete(im,-(n_rows%s_row),0)
if(n_cols%s_col!=0):
    im=np.delete(im,-(n_cols%s_col),1)
n_rows, n_cols=im.shape[0],im.shape[1]

#calculate the avaerage of greyscale pixel values
im_copy=[]
for i in range(0,n_rows,s_row):
    l=[]
    for j in range(0,n_cols,s_col):
        avg=np.sum(im[i:i+s_row,j:j+s_col])/(s_row*s_col)
        l.append(avg)
    im_copy.append(l)
im_copy=np.array(im_copy,dtype=int)
n_rows, n_cols=im_copy.shape[0],im_copy.shape[1]

# print ART
for i in range(n_rows):
    for j in range(n_cols):
        level=int(im_copy[i][j]//(255/l_gs))
        char=gs[level-1]
        print(char,end="")
    print()