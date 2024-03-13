import cv2 
from PIL import Image
import numpy as np
from sys import argv

def get_frames(file)->list:
    vidcap = cv2.VideoCapture(file)
    n=50        #no of frames to extract 
    f = int(vidcap.get(7))
    step=int(f/n)   #steps to take
    print(f,n,step)
    frames_to_get=list(range(0,f,step))
    success,image = vidcap.read()
    count = 0
    while success:
      if(count in frames_to_get):
        cv2.imwrite("./tempfolder/%d.jpg"%count, image)     # save frame as JPEG file      
      success,image = vidcap.read()
      count += 1
    # Release the video capture object
    vidcap.release()
    return frames_to_get

def make_ascii(file,size:int)-> np.array:
    im=np.array(Image.open(file).convert("L"))
    n_rows, n_cols=im.shape[0],im.shape[1]
    gs=" .:-=+*#%@"
    l_gs=len(gs)                            
    s_row,s_col=2*size,size                            

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
    im_char=np.full_like(im_copy,dtype=str,fill_value='.')
    # print ART
    for i in range(n_rows):
        for j in range(n_cols):
            level=int(im_copy[i][j]//(255/l_gs))
            char=gs[level-1]
            im_char[i][j]=char
    return im_char

def write_frame(f, frame: np.array):
    n_rows, n_cols=frame.shape[0],frame.shape[1]
    # print ART
    for i in range(n_rows):
        for j in range(n_cols):
            f.write(frame[i][j])
        f.write('\n')

if __name__ == "__main__":
    vid=argv[1]
    frames_to_get=get_frames(vid)           #get frames
    f=open(f"{vid}.txt","w")                #make a txt file to write all ascii frames
    n_rows=0
    s=int(input("Enter the scale by which to reduce animation size? ")) 
    for im in frames_to_get:
        frame=make_ascii(f"./tempfolder/{im}.jpg",s)
        write_frame(f,frame)
        f.write('101\n')
    f.close()
    print( make_ascii("0.jpg",s).shape[0])
