from moviepy.editor import *
import urllib.request

download_dst = "./inputs/downloaded_countdown.mp4"
print("ダウンロード開始")

urllib.request.urlretrieve(os.getenv("VIDEO_URL"), download_dst)

print("ダウンロード完了")


clip = VideoFileClip("./inputs/downloaded_countdown.mp4").subclip(0, 7)

# osに搭載されているフォントしか使えないので追加で使うときはインストールする必要がある
txt_clip = TextClip("テイクオフ！", font="Takao-Pゴシック", color="white", fontsize=120)
txt_clip = txt_clip.set_position("center").set_duration(4)

video = CompositeVideoClip([clip, txt_clip])

video.write_videofile("./outputs/downloaded_countdown2.mp4",
                      codec="libx264",
                      audio_codec="aac",
                      temp_audiofile="temp-audio.m4a",
                      remove_temp=True)

os.remove(download_dst)
print("ダウンロードファイルを削除")
