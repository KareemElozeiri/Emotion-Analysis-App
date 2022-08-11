import cv2


class Camera:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        self.frame = None 


    def capture(self):
        pass 

    def __del__(self):
        self.camera.release()
        print("Camera Destructor Called")
