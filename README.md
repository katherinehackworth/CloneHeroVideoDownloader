<img src="https://github.com/jshackles/CloneHeroVideoDownloader/raw/master/assets/icon.png" width="32" height="32"></img> Clone Hero Video Downloader
===========
A simple application that allows you to automatically download the top YouTube video result for songs in your Clone Hero library.

What this does
-------
Clone Hero recognises 'video.mp4' file in every song folder as the video to play in the background of the song chart. 
This program recursively runs through your Clone Hero songs folder to find songs that are missing this video.mp4 file. 
If the file is missing, it then searches YouTube and grabs the first result for that song, using the folder name as the search string. If the download of the first search result fails, it attempts to download the second top result. Once downloaded, the file is renamed to 'video.mp4' and placed in the song folder. After this, Clone Hero should automatically recognise the video file and play it during the song.

This program has been tested on very large song libraries with thousands of songs in many nested folders and has been found to be performant.
Please note that because most videos will download in 1080p resolution they can be up to 200MB per video, although most videos tend to be much smaller than that.  
The amount of time it takes to download videos for all of your songs will be highly dependent on your internet speed.  
A progress bar is provided to indicate how many videos still need to be downloaded and will attempt to estimate the time remaining.

This program has also been designed to run multiple times on the same songs directory. If you add new songs to Clone Hero, simply re-run the program and it will only download the videos that are missing.

Should any songs run into errors, this will be displayed once the program has finished running.

Usage
-------
1. [Download the latest release](https://github.com/stripedew/CloneHeroVideoDownloader/releases/latest)
2. Place VideoDownload.exe in your Clone Hero directory (default is C:\Users\XyourusernamehereX\Documents\Clone Hero, one level above your Songs folder)
3. Run VideoDownload.exe

Notes/FAQ
-------
For any songs causing issues, make sure the final folder containing all song files (song.ini etc.) is named 'Artist - song title'. This folder name is where the program gets the artist and song name to search for the video on YouTube.
If you want to replace a video you already have downloaded previously, simply delete or rename the 'video.mp4' file and run the tool again.
