from moviepy import *
import os
import sys
#pip install moviepy

def MP4ToMP3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

VIDEO_FILE_PATH = "/path/path/path/YOUVIDEO.mp4"
AUDIO_FILE_PATH = "/path/path/path/CONVERTED.mp3"

MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)
