import cv2
import math
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
        print('[INFO]: Open camera: FALSE')
        return False
    
    cont = 1
    while(cam.isOpened()):
        frame_id = cam.get(1)        
        ret, frame = cam.read()
        
        if ret != True:
            print('[INFO]: Camera failed')
            break
        
        else:
            if (frame_id % math.floor(frameRate) == 0):                
                filename = path_result + 'camera_' + str(camera_id) + '_' + str(int(cont)) + ".jpg"
                #filename = str(camera_id) + '_' + str(int(cont)) + ".jpg"                
                print('[INFO] Save in: ' + filename)
                cv2.imwrite(filename, frame)
                cont = cont + 1                