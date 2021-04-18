from compoyse.wav.AudioFile import AudioFile
from compoyse.wav.AudioClip import AudioClip
from compoyse.wav.AudioPlayer import AudioPlayer
import os

class Crosstalk:
    def __init__(self):
        self.audio_files = []
        return
    
    def set_parameters(self, parameters):
        self.parameters = parameters
        return

    def perform(self):
        self.read_in_audio_files()
        return
    
    def read_in_audio_files(self):
        file_directory = self.parameters.get_directory_for_files()
        for file in os.scandir(file_directory):
            new_audio_file = AudioFile()
            new_audio_file.set_file_name(file.name)
            new_audio_file.set_file_directory(file_directory)
            self.audio_files.append(new_audio_file)
        return