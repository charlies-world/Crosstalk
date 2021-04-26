import threading

class TrackThread:
    def __init__(self):
        self.thread = threading.Thread()
        return
    
    def set_audio_player(self, audio_player):
        self.audio_player = audio_player
        return
    
    def is_alive(self):
        return self.thread.is_alive()
    
    def start_thread(self, audio_clip):
        self.thread = threading.Thread(target=self.audio_player.play, args=(audio_clip,), daemon=True)
        self.thread.start()
        return
    