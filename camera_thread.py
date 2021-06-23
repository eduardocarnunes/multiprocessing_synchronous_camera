import threading
from utils import util

class CameraThread(threading.Thread):
    def __init__(self, previewName, camID, pathResult):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
        self.pathResult = pathResult
    def run(self):
        print("[INFO]: Starting " + self.previewName)
        util.camera_to_image(self.camID, self.pathResult)