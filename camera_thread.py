import threading
from utils import util

class CameraThreadImage(threading.Thread):
    
    def __init__(self, previewName, camID, pathResult):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
        self.pathResult = pathResult
        
    def run(self):
        print("[INFO]: Starting " + self.previewName)
        util.camera_to_image(self.camID, 
                             self.pathResult)
        
class CameraThreadPreview(threading.Thread):
    
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID        
    
    def run(self):
        print("[INFO]: Starting " + self.previewName)
        util.camera_preview(self.previewName, 
                            self.camID)
        
class CameraThreadPreviewSave(threading.Thread):
    
    def __init__(self, previewName, camID, pathResult, nameVideo):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID   
        self.pathResult = pathResult
        self.nameVideo = nameVideo
        
    def run(self):
        print("[INFO]: Starting " + self.previewName)
        util.show_and_save_video(self.previewName,
                                 self.camID,
                                 self.pathResult,
                                 self.nameVideo)
