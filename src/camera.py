from time import time
import pygame.camera
import pygame.image
from StringIO import StringIO
from PIL import Image

class Camera(object):
    """A generic camera stream with jpeg compression."""

    def __init__(self):
        pygame.camera.init()
        self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
        self.cam.start()

    def __del__(self):
        print "del"
        self.cam.stop()
        pygame.camera.quit()

    def get_frame(self):
        img = self.cam.get_image()
        data = pygame.image.tostring(img, 'RGBA')
        img = Image.fromstring('RGBA', (img.get_width(),img.get_height()), data)
        zdata = StringIO()
        img.save(zdata, 'JPEG')
        return zdata.getvalue()
