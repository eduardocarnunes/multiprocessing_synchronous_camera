# -*- encoding: utf-8 -*-
'''
@File    : util.py
@Time    : 2021/07/06 20:48:54
@Author  : Eduardo Carvalho nunes
@Contact : TWA: eduardo.carvaho@twa.pt
 Personal: eduardocarvalho-1992@hotmail.com
@Desc    : None
'''
# import libraries
import cv2
import math
import numpy as np
import glob
from datetime import datetime
# import my libraries
from utils import config


def camera_to_image(camera_id, path_result):
    """Convert camera in real time for image

    Args:
        camera_id (int): ID of camera. Example: Usually ID WebCam is 0.
        path_result (string): Path where will save of images.
    """
    # open camera
    cam = cv2.VideoCapture(camera_id)

    print('[INFO]: Press ESC for exit or stop')
    counter = 1

    while(True):
        ret, frame = cam.read()

        if not ret:
            print('[INFO]: Camera failed. Camera ID: ' + str(camera_id))
            break

        else:
            filename = path_result + 'camera_' + \
                str(camera_id) + '_' + str(int(cont)) + ".jpg"
            print('[INFO] Save in: ' + filename)
            cv2.imwrite(filename, frame)
            counter = counter + 1

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cam.release()

    cv2.destroyAllWindows()


def camera_preview(name_preview, camera_id):
    """Show came live

    Args:
        name_preview (string): name of camera. Example: Camera 1
        camera_id (int): id of camera.
    """
    # open camera
    cam = cv2.VideoCapture(camera_id)

    # get fps of camera
    fps = cam.get(cv2.CAP_PROP_FPS)
    print(
        "Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    # define some settings
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (0, 0, 255)
    thickness = 2

    print('[INFO]: Press ESC for exit or stop')

    while(1):
        #frame_id = cam.get(1)
        ret, frame = cam.read()

        if not ret:
            print('[INFO]: Camera failed. Camera ID: ' + str(camera_id))
            break

        else:
            h, w, c = frame.shape
            frame = cv2.putText(frame, name_preview, (10, 25), font, fontScale,
                                color, thickness, cv2.LINE_AA)

            current_time = str(datetime.now())

            frame = cv2.putText(
                frame,
                current_time,
                (10,
                 h - 15),
                font,
                fontScale,
                color,
                thickness,
                cv2.LINE_AA)
            cv2.imshow(name_preview, frame)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()


def images_to_video(path_images, path_result, name_video):
    """convert images to video

    Args:
        path_images (string): path of images
        path_result (string): path result of video
        name_video (string): name of video for save
    """

    path = path_images + '*.jpg'
    image_array = []

    # read all images in a folder and add in a list
    for filename in glob.glob(path):
        image = cv2.imread(filename)
        height, width, layers = image.shape
        size = (width, height)
        image_array.append(image)

    # create VideoWriter
    out = cv2.VideoWriter(
        path_result + name_video,
        cv2.VideoWriter_fourcc(
            *'DIVX'),
        config.FRAME_RATE,
        size)

    for i in range(len(image_array)):
        out.write(image_array[i])
    out.release()

    print('[INFO]: Video save in: ' + path_result + name_video)


def show_and_save_video(
        name_preview,
        camera_id,
        path_result_video,
        name_video):
    """show camera live and save this live in a file

    Args:
        name_preview (string): name of camera. Example: Camera 1
        camera_id (int): camera id
        path_result_video (string): path where will save of video
        name_video (string): name of file video. Example: video.mp4
    """

    # This will return video from the first webcam on your computer.
    cap = cv2.VideoCapture(camera_id)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(
        path_result_video +
        name_video,
        fourcc,
        config.FRAME_RATE,
        config.SIZE)

    # define some settings
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

        # settings text in frame
        frame = cv2.putText(frame, name_preview, (10, 25), font, fontScale,
                            color, thickness, cv2.LINE_AA)

        # get current data and hour
        current_time = str(datetime.now())

        # define text
        frame = cv2.putText(frame, current_time, (10, h - 15), font, fontScale,
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
