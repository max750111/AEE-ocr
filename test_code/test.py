from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *
import math
#
input_video_path = 'all.mp4'
output_video_path = 'part.mp4'
clip = VideoFileClip("all.mp4")

print(clip.duration)
t1, t2 = 0, clip.duration/4
for i in range(0,4):
    t1, t2 = math.floor(0+clip.duration/4*i), math.floor(clip.duration / 4 +clip.duration/4*i)-1
    ffmpeg_extract_subclip(input_video_path, t1, t2, targetname='part'+str(i+1)+'.mp4')
    print(t1, t2)


