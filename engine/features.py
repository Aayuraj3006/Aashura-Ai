
from playsound import playsound
import eel


@eel.expose
# Audio file path
def playAssistantSound():
    music_dir = r'P:\aashura\www\assets\audio\start_sound.mp3'
    playsound(music_dir)