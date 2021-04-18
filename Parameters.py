class Parameters:
    def __init__(self):
        self.directory_for_files = ''
        self.minimum_length_of_piece = 0
        self.maximum_length_of_piece = 0
        self.number_of_tracks = 0
        self.chance_that_next_track_will_play = 0
        self.minimum_length_of_clip = 0
        self.maximum_length_of_clip = 0
        self.minimum_length_between_checks = 0
        self.maximum_length_between_checks = 0
        return
    
    def get_directory_for_files(self):
        return self.directory_for_files
    
    def get_minimum_length_of_piece(self):
        return self.minimum_length_of_piece
    
    def get_maximum_length_of_piece(self):
        return self.maximum_length_of_piece
    
    def get_number_of_tracks(self):
        return self.number_of_tracks
    
    def get_chance_that_next_track_will_play(self):
        return self.chance_that_next_track_will_play
    
    def get_minimum_length_of_clip(self):
        return self.minimum_length_of_clip
    
    def get_maxium_length_of_clip(self):
        return self.maximum_length_of_clip
    
    def get_minimum_length_between_checks(self):
        return self.minimum_length_between_checks
    
    def get_maximum_length_between_checks(self):
        return self.maximum_length_between_checks
    
    def set_directory_for_files(self, directory_for_files):
        self.directory_for_files = directory_for_files
        return
    
    def set_minimum_length_of_piece(self, minimum_length_of_piece):
        self.minimum_length_of_piece = minimum_length_of_piece
        return
    
    def set_maximum_length_of_piece(self, maximum_length_of_piece):
        self.maximum_length_of_piece = maximum_length_of_piece
        return
    
    def set_number_of_tracks(self, number_of_tracks):
        self.number_of_tracks = number_of_tracks
        return
    
    def set_chance_that_next_track_will_play(self, chance_that_next_track_will_play):
        self.chance_that_next_track_will_play = chance_that_next_track_will_play
        return
    
    def set_minimum_length_of_clip(self, minimum_length_of_clip):
        self.minimum_length_of_clip = minimum_length_of_clip
        return
    
    def set_maximum_length_of_clip(self, maximum_length_of_clip):
        self.maximum_length_of_clip = maximum_length_of_clip
        return
    
    def set_minimum_length_between_checks(self, minimum_length_between_checks):
        self.minimum_length_between_checks = minimum_length_between_checks
        return
    
    def set_maximum_length_between_checks(self, maximum_length_between_checks):
        self.maxiumum_length_between_checks = maximum_length_between_checks
        return