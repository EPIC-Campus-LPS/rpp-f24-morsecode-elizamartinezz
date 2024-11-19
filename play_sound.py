import pydub
import os
import glob
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("jinglebellz.mp3")
play(song)
