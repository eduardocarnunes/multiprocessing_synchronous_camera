import argparse

import camera_thread
from utils import config          
from utils import util


ap = argparse.ArgumentParser()
ap.add_argument("-option", "--opt", required=False,
                help="-p: preview, -c: capture, -video: images to video")
#ap.add_argument("-c", "--capture", required=False,
#                help="capture images and save")
#ap.add_argument("-v", "--video", required=False,
                #help="convert images to videoe")
args = vars(ap.parse_args())
        
if args['opt'] == 'preview':       
    # Create threads as follows
    # Thread 1 for camera 1. Save image 
    thread1 = camera_thread.CameraThreadImage("Camera 1", 0, config.IMAGE_RESULT_PATH_CAMERA_1)
    # Thread 2 for camera 2. Save image 
    thread2 = camera_thread.CameraThreadImage("Camera 2", 1, config.IMAGE_RESULT_PATH_CAMERA_2)
    # Execute 
    thread1.start()
    thread2.start()

if args['opt'] == 'capture':    
    # Thread 3 for show display camera 1
    thread3 = camera_thread.CameraThreadPreview("Camera 1", 0)
    # Thread 4 for show display camera 2
    thread4 = camera_thread.CameraThreadPreview("Camera 2", 1)
    # Execute
    thread3.start()
    thread4.start()


if args['opt'] == 'video':
    # Images to video (Camera 1)
    util.images_to_video(config.IMAGE_RESULT_PATH_CAMERA_1, 
                         config.VIDEO_RESULT_PATH_CAMERA_1,
                         'video_camera_1.avi')
    
    # Images to video (Camera 2)
    util.images_to_video(config.IMAGE_RESULT_PATH_CAMERA_2, 
                         config.VIDEO_RESULT_PATH_CAMERA_2,
                         'video_camera_2.avi')
    

