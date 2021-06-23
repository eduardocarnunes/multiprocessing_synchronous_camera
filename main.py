import camera_thread
from utils import config          
        
# Create threads as follows
thread1 = camera_thread.CameraThread("Camera 1", 1, config.IMAGE_RESULT_PATH_CAMERA_1)
thread2 = camera_thread.CameraThread("Camera 2", 2, config.IMAGE_RESULT_PATH_CAMERA_2)

thread1.start()
thread2.start()
