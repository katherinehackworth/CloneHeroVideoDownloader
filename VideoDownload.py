import configparser
import glob
import os
import time
import yt_dlp
from tqdm import tqdm
from youtubesearchpython import VideosSearch

homeFolder = os.path.abspath(os.getcwd() + "\\songs")
os.chdir(homeFolder)
videotitle=''
i=0
erroredSongs = []

for filename in glob.iglob(homeFolder + "/**/song.ini", recursive=True):
	i+=1

while True:
	with tqdm(total=i,unit="videos") as pbar:
		try:
			for filename in glob.iglob(homeFolder + "/**/song.ini", recursive=True):
				currentSongFileFolder = os.path.dirname(filename)
				currentSongName = os.path.basename(currentSongFileFolder)
				os.chdir(currentSongFileFolder)
				time.sleep (0.0001)
				pbar.update(1)

				if not os.path.exists("video.mp4"):
					query = 'Youtube {} (Official Music Video)'.format(currentSongName)

					# scrapes the URL from YouTube
					youtube = VideosSearch(query, limit = 1).result()
					url = youtube['result'][0]['link']
					videoTitle = youtube['result'][0]['title']
					print("\nNow downloading: " + videoTitle)

					# downloads the song
					ydl_opts = {'outtmpl': 'video.mp4',
							'format': 'mp4',
							'nooverwrites': 0,
							'noplaylist': 1,
							'quiet': True}
					with yt_dlp.YoutubeDL(ydl_opts) as ydl:
						ydl.download([url])
					with open('song.ini') as songCheck:
						# check if the ini file contains unexpected phase shift converter text
						if '//Converted' in songCheck.read():
							erroredSongs.append(filename)
						else: 
							# change the song.ini file to attempt to sync the video
							config = configparser.ConfigParser()
							config.read('song.ini')
							config.set('song', 'video_start_time', '-3000')

							with open('song.ini', 'w') as configfile:
								config.write(configfile)
		except Exception as e:
			print(e)
			print("Error on song: " + videoTitle + ". Skipping")
			continue
		else:
			break
if erroredSongs:
	print("The following songs had errors:")
	for i in erroredSongs:
		print(i, end='\n')
input("Video download complete.  Press Enter to exit.")




