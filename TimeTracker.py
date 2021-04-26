from time import time

class TimeTracker:
    def __init__(self,
                 minimum_length_of_piece,
                 maximum_length_of_piece):
        self.minimum_length_of_piece = minimum_length_of_piece
        self.maximum_length_of_piece = maximum_length_of_piece
        self.start_time = time()
        return
    
    def set_current_time(self):
        self.current_time = time() - self.start_time
        return
    
    def current_time_is_less_than_minimum_length(self):
        if(self.current_time < self.minimum_length_of_piece):
            return True
        else:
            return False
    
    def current_time_is_greater_than_maximum_length(self):
        if(self.current_time > self.maximum_length_of_piece):
            return True
        else:
            return False
        