<img src="https://github.com/jshackles/CloneHeroVideoDownloader/raw/master/assets/icon.png" width="32" height="32"></img> Clone Hero Video Downloader
===========
An application that allows you to download the top YouTube music video for songs in your Clone Hero library.
Forked and updated as original stopped working. 

What this does
-------
This program will recursively run through your Clone Hero songs folder to find songs that are missing a video.mp4 file.  It will then search YouTube for the top result for that song name (based on folder name), and then download that YouTube video and place it in the directory. The end result will be that when playing that song in Clone Hero, the background will be the music video of that song.

This program has been tested on very large song libraries with thousands of songs in many nested folders and has been found to be performant.  Please note that because most videos will download in 1080p resolution they can be up to 200MB per video.  The amount of time it takes to download videos for all of your songs will be highly dependent on your internet speed.  A progress bar is provided to indicate how many videos still need to be downloaded and will attempt to estimate the time remaining.

This program has also been designed to run multiple times on the same songs directory.  So, if you add new songs to Clone Hero, simply re-run the program and it will only download the videos that are missing.

Should any songs run into errors, this will be displayed once the program has finished running.

Usage
-------
1. [Download the latest release](https://github.com/stripedew/CloneHeroVideoDownloader/releases/latest)
2. Place VideoDownload.exe in your Clone Hero directory (default is C:\Users\XyourusernamehereX\Documents\Clone Hero, one level above your Songs folder)
4. Run VideoDownload.exe

NOTES
-------
For any songs causing issues, make sure the final folder containing all song files (song.ini etc.) is named 'Artist - song title'. This folder name is where the program gets the artist and song name to search for the video on YouTube.
