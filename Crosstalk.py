from compoyse.wav.AudioFile import AudioFile
from compoyse.wav.AudioClip import AudioClip
from compoyse.wav.AudioPlayer import AudioPlayer
from TimeTracker import TimeTracker
from TrackThread import TrackThread
import os
from time import time, sleep
import random
import threading
from Parameters import Parameters

class Crosstalk:
    def __init__(self, parameters):
        self.perform(parameters)
        return

    def perform(self, parameters):
        audio_files = self.read_in_audio_files(parameters.get_directory_for_files())
        tracks_threads = self.create_tracks_threads(parameters.get_number_of_tracks())
        done = False
        time_tracker = TimeTracker(parameters.get_minimum_length_of_piece(), 
                                   parameters.get_maximum_length_of_piece())
        
        while not done:
            a_track_should_play = self.decide_if_a_track_should_play(tracks_threads, parameters.get_chance_that_next_track_will_play())
            if(a_track_should_play):
                self.play_new_track(audio_files, 
                                    tracks_threads, 
                                    parameters.get_minimum_length_of_clip(), 
                                    parameters.get_maximum_length_of_clip())
            self.pause(parameters.get_minimum_length_between_checks(), parameters.get_maximum_length_between_checks())
            done = self.decide_if_piece_is_done(time_tracker,
                                                parameters.get_minimum_length_of_piece(),
                                                parameters.get_maximum_length_of_piece())
            
        return
    
    def read_in_audio_files(self, file_directory):
        audio_files=[]
        for file in os.scandir(file_directory):
            new_audio_file = AudioFile()
            new_audio_file.set_file_name(file.name)
            new_audio_file.set_file_directory(file_directory)
            audio_files.append(new_audio_file)
        return audio_files
    
    def create_tracks_threads(self, number_of_tracks):
        tracks_threads = []
        audio_player = AudioPlayer()
        for i in range(0, number_of_tracks):
            new_track_thread = TrackThread()
            new_track_thread.set_audio_player(audio_player)
            tracks_threads.append(new_track_thread)
        return tracks_threads
    
    def decide_if_a_track_should_play(self, tracks_threads, chance_that_next_track_will_play):
        if(self.not_at_maximum_number_of_tracks(tracks_threads)):
            if(self.get_random_integer_between(0, chance_that_next_track_will_play)):
                return True
            else:
                return False
        
    def not_at_maximum_number_of_tracks(self, tracks_threads):
        for i in range(0, len(tracks_threads)):
            if(tracks_threads[i].is_alive() is False):
                return True
        return False
    
    def play_new_track(self, audio_files, 
                       tracks_threads,
                       minimum_length_of_clip,
                       maximum_length_of_clip):
        audio_clip_to_play = AudioClip()
        
        audio_file_to_play = self.get_random_audio_file(audio_files)
        audio_clip_to_play.set_audio_file(audio_file_to_play)
        
        audio_clip_start = self.get_random_integer_between(0, audio_file_to_play.get_duration())
        audio_clip_to_play.set_start(audio_clip_start)
        
        audio_clip_to_play_duration_of_playtime = self.get_random_integer_between(minimum_length_of_clip, maximum_length_of_clip)
        time_between_audio_clip_start_and_file_end = audio_file_to_play.get_duration() - audio_clip_start
        if(time_between_audio_clip_start_and_file_end < audio_clip_to_play_duration_of_playtime):
            audio_clip_to_play_duration_of_playtime = time_between_audio_clip_start_and_file_end
        audio_clip_to_play.set_duration_of_playtime(audio_clip_to_play_duration_of_playtime)
        
        thread_to_play_in = self.get_a_thread_thats_not_executing(tracks_threads)
        thread_to_play_in.start_thread(audio_clip_to_play)
        return
    
    def get_random_audio_file(self, audio_files):
        index_of_random_file = self.get_random_integer_between(0, len(audio_files))
        return audio_files[index_of_random_file]
    
    def get_a_thread_thats_not_executing(self, tracks_threads):
        for i in range(0, len(tracks_threads)):
            if(tracks_threads[i].is_alive() is False):
                return tracks_threads[i]
    
    def decide_if_piece_is_done(self, 
                                time_tracker,
                                minimum_length_of_piece,
                                maximum_length_of_piece):
        time_tracker.set_current_time()
        if(time_tracker.current_time_is_less_than_minimum_length()):
            return False
        elif(time_tracker.current_time_is_greater_than_maximum_length()):
            return True
        else:
            return self.randomly_decide_if_piece_is_done(minimum_length_of_piece, maximum_length_of_piece)
        
    def randomly_decide_if_piece_is_done(self,
                                         minimum_length_of_piece,
                                         maximum_length_of_piece):
        chance_that_piece_is_done = maximum_length_of_piece - minimum_length_of_piece
        if(self.get_random_integer_between(0, chance_that_piece_is_done) == 0):
            return True
        else:
            return False
          
    def pause(self, minimum_length_between_checks, maximum_length_between_checks):
        length_of_time_to_pause = self.get_random_integer_between(minimum_length_between_checks, maximum_length_between_checks)
        sleep(length_of_time_to_pause)
        return
    
    def get_random_integer_between(self, value1, value2):
        value1 = int(value1)
        value2 = int(value2)
        return random.randrange(value1, value2)