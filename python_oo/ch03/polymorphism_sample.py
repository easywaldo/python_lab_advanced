from pathlib import Path

class AudioFile:
    ext: str
    
    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == self.ext:
            raise ValueError("Invalid file format")
        self.filepath = filepath
        
class MP3File(AudioFile):
    ext = ".mp3"
    
    def play(self) -> None:
        print(f"playing {self.filepath} as mp3")
        
    
class WavFile(AudioFile):
    ext = ".wav"
    
    def play(self) -> None:
        print(f"playing {self.filepath} as wav")
        

class OggFile(AudioFile):
    ext = ".ogg"
    
    def play(self) -> None:
        print(f"playing {self.filepath} as ogg")

p_1 = MP3File(Path("Heart of the Sunrise.mp3"))
p_1.play()

p_2 = WavFile(Path("my piano playing file.wav"))
p_2.play()

p_3 = OggFile(Path("my music instruments file.ogg"))
p_3.play()

# p_4 = MP3File(Path("wrong file.mov"))
# p_4.play()


class FileChat:
    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == ".flac":
            raise ValueError("Not a .flac file")
        self.filepath = filepath
    
    def play(self) -> None:
        print(f"playing {self.filepath} as falc")


wrong_chat_file = FileChat(Path("wrong audio file.flac"))
wrong_chat_file.play()
