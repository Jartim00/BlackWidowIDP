#!/usr/bin/python
import pygame.camera
import pygame.image
class Camera(object):
    def __init__(self):
        print "init"
        pygame.camera.init()
        self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
        self.cam.start()
    def __del__(self):
        print "del"
        self.cam.stop()
        pygame.camera.quit()
    def takeImage(self):
        img = self.cam.get_image()
        pygame.image.save(img, "photo.jpg")
camera = Camera()
camera.takeImage()
