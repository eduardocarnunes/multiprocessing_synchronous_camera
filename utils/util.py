import cv2
import math
import numpy as np
import glob

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
    frameRate = cam.get(config.FRAME_RATE) 
    
    if cam.isOpened():
        ret, frame = cam.read()
        print('[INFO]: Open camera: TRUE')
    else:
        print('[INFO]: Open camera: FALSE. Camera ID: ' + str(camera_id))
        return False
    
    print('[INFO]: Press ESC for exit or stop')
    cont = 1
    while(1):
        frame_id = cam.get(1)        
        ret, frame = cam.read()
        
        if ret != True:
            print('[INFO]: Camera failed. Camera ID: ' + str(camera_id))
            break
        
        else:
            if (frame_id % math.floor(frameRate) == 0):                
                filename = path_result + 'camera_' + str(camera_id) + '_' + str(int(cont)) + ".jpg"
                #filename = str(camera_id) + '_' + str(int(cont)) + ".jpg"                
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
    frameRate = cam.get(config.FRAME_RATE) 

    print('[INFO]: Press ESC for exit or stop')
    while(1):
        frame_id = cam.get(1)
        ret, frame = cam.read()
        
        if ret != True:
            print('[INFO]: Camera failed. Camera ID: ' + str(camera_id))
            break
        
        else:
            if (frame_id % math.floor(frameRate) == 0):                                
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
        