import cv2
import math
import numpy as np
import glob
from datetime import datetime

from utils import config

def camera_to_image(camera_id, path_result):
    """   

    Parameters
    ----------
    camera_id : TYPE
        DESCRIPTION.
    frame_rate : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """    
    
    cam = cv2.VideoCapture(camera_id)    
    
    print('[INFO]: Press ESC for exit or stop')
    cont = 1
    while(True):
        ret, frame = cam.read()
        
        if ret != True:
            print('[INFO]: Camera failed. Camera ID: ' + str(camera_id))
            break
        
        else:
            filename = path_result + 'camera_' + str(camera_id) + '_' + str(int(cont)) + ".jpg"
            
            print('[INFO] Save in: ' + filename)            
            cv2.imwrite(filename, frame)
            cont = cont + 1                
        
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        
    cam.release()
    
    cv2.destroyAllWindows()
                
                
def camera_preview(name_preview, camera_id):
    """
    

    Parameters
    ----------
    name_preview : TYPE
        DESCRIPTION.
    camera id : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    cam = cv2.VideoCapture(camera_id)
    #frameRate = cam.get(config.FRAME_RATE) 
        
    fps = cam.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (0, 0, 255)
    thickness = 2

    print('[INFO]: Press ESC for exit or stop')
    while(1):
        #frame_id = cam.get(1)
        ret, frame = cam.read()
        
        if ret != True:
            print('[INFO]: Camera failed. Camera ID: ' + str(camera_id))
            break
        
        else:
            h, w, c = frame.shape    
            #print('[INFO]: Height: ' + str(h) + ' Width: ' + str(w))
            #p1 = (5,5)
            #p2 = (150,30)
            #frame = cv2.rectangle(frame, p1, p2, (0, 0, 255), 2)
            frame = cv2.putText(frame, name_preview, (10,25), font, fontScale,
                                color, thickness, cv2.LINE_AA)
            
            current_time = str(datetime.now())
            #print(current_time)
            
            frame = cv2.putText(frame, current_time, (10,h-15), font, fontScale,
                                color, thickness, cv2.LINE_AA)
            cv2.imshow(name_preview, frame)
                
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        
    cam.release()
    cv2.destroyAllWindows()
    
def images_to_video(path_images, path_result, name_video):
    
    path = path_images + '*.jpg'
    image_array = []
    
    for filename in glob.glob(path):
        image = cv2.imread(filename)
        height, width, layers = image.shape
        size = (width,height)
        image_array.append(image)
        
    out = cv2.VideoWriter(path_result + name_video, cv2.VideoWriter_fourcc(*'DIVX'), config.FRAME_RATE, size)
    
    for i in range(len(image_array)):
        out.write(image_array[i])
    out.release()
    
    print('[INFO]: Video save in: ' + path_result + name_video)
    
def show_and_save_video(name_preview, camera_id, path_result_video, name_video):
    
    # This will return video from the first webcam on your computer.
    cap = cv2.VideoCapture(camera_id)  
  
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(path_result_video + name_video, fourcc, config.FRAME_RATE, config.SIZE)

    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (0, 0, 255)
    thickness = 2
    
  
    # loop runs if capturing has been initialized. 
    while(True):
        # reads frames from a camera 
        # ret checks return at each frame
        ret, frame = cap.read()  
        
        h, w, c = frame.shape
        
        frame = cv2.putText(frame, name_preview, (10,25), font, fontScale,
                                color, thickness, cv2.LINE_AA)
            
        current_time = str(datetime.now())
            
        frame = cv2.putText(frame, current_time, (10,h-15), font, fontScale,
                                color, thickness, cv2.LINE_AA)
       
        # output the frame
        out.write(frame) 
          
        # The original input frame is shown in the window 
        cv2.imshow(name_preview, frame)
          
        # Wait for 'ESC' key to stop the program 
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
  
    # Close the window / Release webcam
    cap.release()
      
    # After we release our webcam, we also release the output
    out.release() 
      
    # De-allocate any associated memory usage 
    cv2.destroyAllWindows()
    
    
        