# -*- encoding: utf-8 -*-
'''
@File    : camera_thread.py
@Time    : 2021/07/06 22:10:42
@Author  : Eduardo Carvalho nunes
@Contact : TWA: eduardo.carvaho@twa.pt
 Personal: eduardocarvalho-1992@hotmail.com
@Desc    : None
'''

# import libraries
import threading
# import my libraries
from utils import util


class CameraThreadImage(threading.Thread):
    """Each Camera should has a thread

    Args:
        threading (Thread): thread
    """

    def __init__(self, preview_name, cam_id, path_result):
        threading.Thread.__init__(self)
        self.preview_name = preview_name
        self.cam_id = cam_id
        self.path_result = path_result

    def run(self):
        print("[INFO]: Starting " + self.preview_name)
        util.camera_to_image(self.cam_id,
                             self.path_result)


class CameraThreadPreview(threading.Thread):
    """Each Camera should has a thread

    Args:
        threading (Thread): thread
    """

    def __init__(self, preview_name, cam_id):
        threading.Thread.__init__(self)
        self.preview_name = preview_name
        self.cam_id = cam_id

    def run(self):
        print("[INFO]: Starting " + self.preview_name)
        util.camera_preview(self.preview_name,
                            self.cam_id)


class CameraThreadPreviewSave(threading.Thread):
    """Each Camera should has a thread

    Args:
        threading (Thread): thread
    """

    def __init__(self, preview_name, cam_id, path_result, name_video):
        threading.Thread.__init__(self)
        self.preview_name = preview_name
        self.cam_id = cam_id
        self.path_result = path_result
        self.name_video = name_video

    def run(self):
        print("[INFO]: Starting " + self.preview_name)
        util.show_and_save_video(self.preview_name,
                                 self.cam_id,
                                 self.path_result,
                                 self.name_video)
