import cv2
from UI.UI import UI


class App:
    def __init__(self)->None:
        self.UI = UI() 

    '''
        open the UI and starts the functions of the application
    '''
    def start(self)->None:
        self.UI.run()

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