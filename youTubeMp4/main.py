import pytube
from pytube import YouTube
import os
import sys
#take the input from the user

url = input("Enter the url you want to download: \n>>")
video = YouTube(str(url))

#
def load_Progress(stream,chunk,bytes_remaining,suffix = ''):
    barLenght = 60
    filledLength = int(round(barLenght*bytes_remaining/ float(stream.filesize)))
    bytes_dowloaded = stream.filesize - bytes_remaining
    percent = round(bytes_dowloaded*100/stream.filesize,1)
    bar = '#'* filledLength + '-'*(barLenght-filledLength)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar,percent, '%', suffix))
    sys.stdout.flush()

#destination to save the file
destination = "C:"

#download the file
video.register_on_progress_callback(load_Progress)
downloaded_file = pytube.YouTube(url).streams.get_highest_resolution().download(destination)


#result of success
print( video.title +" has benn succesfully downloaded ")
