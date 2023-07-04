from pygame import mixer
from gtts import gTTS

def main():
    tts = gTTS('KANISTER allows domain experts to capture application specific data management tasks in blueprints which can be easily shared and extended. The framework takes care of the tedious details around execution on Kubernetes and presents a homogeneous operational experience across applications at scale.')
    tts.save('output.mp3')
    mixer.init()
    mixer.music.load('output.mp3')
    mixer.music.play()

if __name__ == "__main__":
    main()