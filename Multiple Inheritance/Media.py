# 7. Create a base class Media. Derive Audio and Video from it. 
#    Then create Multimedia that inherits from both Audio and Video 
#    and plays all types of media.

class Media:
    def __init__(self,name):
        self.name = name
class Audio(Media):
    def work(self):
        print(f"{self.name} PLays SOngs")
class Video(Media):
    def work(self):
        print(f"{self.name} Plays Videos")

class Multimedia(Audio,Video):
    def work(self):
        print(F"{self.name} Has Movies")

Audio = Audio("Audio")
Video = Video("Video")
Multimedia = Multimedia("Multimedia")

Video.work()
Audio.work()
Multimedia.work()
