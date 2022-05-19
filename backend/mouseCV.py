import cv2


LEFT_DOWN = cv2.EVENT_LBUTTONDOWN
RIGHT_DOWN = cv2.EVENT_RBUTTONDOWN
LEFT_UP = cv2.EVENT_LBUTTONUP
RIGHT_UP = cv2.EVENT_RBUTTONUP
MOVE = cv2.EVENT_MOUSEMOVE

LEFT_CLICK = 'left_click'
RIGHT_CLICK = 'right_click'
LEFT_MOVE = 'left_move'
RIGHT_MOVE = 'right_move'
NONE = 'none'

class Mouse:
    
    def __init__(self, name):
        self.status = None
        self.pre_event = NONE
        self.x, self.y = 0, 0
        self.name = name
        cv2.setMouseCallback(self.name, self.event)

    def set_window(self, name):
        cv2.setMouseCallback(name, self.event)
    
    
    def event(self, event,x,y,flags,param):
        self.status = event
        self.x,self.y = x,y
        
    
    def get_status(self):
        st = self.status
        if self.status != MOVE:
            self.status = -1
        return st

    def event2(self, event,x,y,flags,param):
        if event in [cv2.EVENT_LBUTTONDOWN, cv2.EVENT_RBUTTONUP] :
            self.status = NONE
        
        elif self.pre_event == cv2.EVENT_LBUTTONDOWN:
            if event == cv2.EVENT_MOUSEMOVE:
                self.status = LEFT_MOVE
            
            elif event == cv2.EVENT_LBUTTONUP:
                self.status = LEFT_CLICK
                
        elif self.pre_event == cv2.EVENT_RBUTTONDOWN:
            if event == cv2.EVENT_MOUSEMOVE:
                self.status = RIGHT_MOVE
            
            elif event == cv2.EVENT_RBUTTONUP:
                self.status = RIGHT_CLICK
                
        else:
            self.event = NONE
                
        self.pre_event = event    
        self.x,self.y = x,y
        