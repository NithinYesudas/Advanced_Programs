from moviepy.editor import *
import requests
# Load the video file
video = VideoFileClip("D:\Blender animation team_71-74.mp4") # You can also use a URL  

# Extract the audio from the video
audio = video.audio

# Save the audio to a file
audio.write_audiofile("D:/audio12.mp3") 

