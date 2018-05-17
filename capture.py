import os
import uuid
import json
import request

from time import sleep
from picamera import PiCamera

WAIT_TIME = 300 # 5 minutes
PICTURES_FOLDER = os.path.join('/', 'tmp')
UPLOAD_URL = 'http://localhost:5000/api/v1/media?deviceId='

while true:
    def take_picture():
        camera = PiCamera()
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        sleep(2)
        filename = os.path.join(PICTURES_FOLDER, str(uuid.uuid1()) + '.jpg')
        camera.capture(filename)
        return filename

    def upload_picture(filepath):
        files = { 'file': open(filepath, 'rb') }
        res = requests.post(UPLOAD_URL, files=files)
        return res

    picture_file = take_picture()
    upload_picture(picture_file)

    time.sleep(WAIT_TIME)

