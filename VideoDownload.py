import configparser
import glob
import os
import time
import yt_dlp
from tqdm import tqdm
from youtubesearchpython import VideosSearch

def clean_cookie():
	if os.path.exists(".google-cookie"):
		os.remove(".google-cookie")

clean_cookie()		

print('Checking for home folder')
songsFolder = os.getcwd() + "\\songs"

if os.path.exists(songsFolder):
	print('Songs folder found')
	homeFolder = os.path.abspath(os.getcwd() + "\\songs")
	os.chdir(homeFolder)

	videotitle=''
	i=0
	erroredSongs = []

	for filename in glob.iglob(homeFolder + "/**/song.ini", recursive=True):
		i+=1

	totalcount = i

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
						query = '{} (Official Music Video)'.format(currentSongName)
						print('\nLooking on YouTube for: ' + query)

						# finds the video URL from YouTube
						youtube = VideosSearch(query, limit = 1).result()
						url = youtube['result'][0]['link']
						videoTitle = youtube['result'][0]['title']
						print("\nSearch success. Now downloading: " + videoTitle)

						# downloads the song
						ydl_opts = {'outtmpl': 'video.mp4',
								'format': 'mp4',
								'nooverwrites': 0,
								'noplaylist': 1,
								'quiet': True,
								'ignoreerrors': True}
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
								# Check uppercase/lowercase config section name
								if config.has_section('song'):
									config.set('song', 'video_start_time', '-3000')
								elif config.has_section('Song'):
									config.set('Song', 'video_start_time', '-3000')
								else:
									print('Could not update song.ini. Check the song.ini for potential issues')
									erroredSongs.append(filename)
								with open('song.ini', 'w') as configfile:
									config.write(configfile)
						clean_cookie()
			except Exception as e:
				print(e)
				print("Error downloading song: " + videoTitle + ". Skipping")
				erroredSongs.append(videoTitle)
				continue
			else:
				break

	if erroredSongs:
		print("The following videos were downloaded but not audio-synced")
		for i in erroredSongs:

			print(i, end='\n')
	input("All downloads complete. Checked a total of " + str(totalcount)+ " songs. Press any button to exit.")
else:
	input("Did not detect a 'Songs' folder. Check you have placed the .exe file in the directory one level above it. Press any button to exit")



