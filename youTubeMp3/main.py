from pytube import YouTube
import os

#take the input from the user

yt = YouTube(str(input("Enter the url you want to download: \n>>")))

#extract only audio
video = yt.streams.filter(only_audio=True).first()

#destination to save the file
print("Enter the destination path(leave the blank for the current directory)")
destination = str(input(">>")) or '.'

#download the file
downloaded_file = video.download(output_path=destination)

#save the file
base, ext = os.path.splitext(downloaded_file)
new_file = base + '.mp4'
os.rename(downloaded_file, new_file)

#result of success
print(yt.title + " has benn succesfully"
                 " downloaded un .mp3 format.")