from moviepy.editor import *

clip = VideoFileClip("./inputs/takeoff.mp4").subclip(0, 7)

txt_clip = TextClip("テイクオフ！", font="Takao-Pゴシック", color="white", fontsize=120)
txt_clip = txt_clip.set_position("center").set_duration(4)

video = CompositeVideoClip([clip, txt_clip])

video.write_videofile("./outputs/edited_takeoff.mp4",
                      codec="libx264",
                      audio_codec="aac",
                      temp_audiofile="temp-audio.m4a",
                      remove_temp=True)


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
