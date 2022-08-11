import cv2
from GUI.GUI import GUI
from src.Camera import Camera


class App:
    def __init__(self)->None:
        self.GUI = GUI() 
        self.Camera = Camera()

    '''
        open the UI and starts the functions of the application
    '''
    def start(self)->None:
        self.GUI.run()

    '''
        ends the life cycle of the application 
    '''
    def terminate(self)->None:
        pass 

    '''
        saves the statistics to the database 
    '''
    def save_statistics(self):
        pass 
    
    '''
        imports the statistics of the user
    '''
    def get_statistics(self):
        pass 

    
    

if __name__ == "__main__":
    pass 