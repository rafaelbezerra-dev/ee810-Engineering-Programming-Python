#! /usr/bin/python

import vlc
import pafy #https://github.com/mps-youtube/pafy

instance = vlc.Instance('--fullscreen')

# url = "https://www.youtube.com/watch?v=_V7ZKk-NJVA"
url = "https://www.youtube.com/watch?v=OPf0YbXqDm0"
video = pafy.new(url)
# FOR VIDEO STREAM
best = video.getbest()
# FOR AUDIO STREAM
# bestaudio = video.getbestaudio()
movie = best.url

#movie is the YouTube or a local URL
media = instance.media_new(movie)
media_list = instance.media_list_new([movie]) #A list of one movie

player = instance.media_player_new()
player.set_media(media)

#Create a new MediaListPlayer instance and associate the player and playlist with it

list_player =  instance.media_list_player_new()
list_player.set_media_player(player)
list_player.set_media_list(media_list)


try:
    player.play()
    player.pause()
    while True:
        pass
except KeyboardInterrupt:
    player.stop()
    print "tchau"
except:
    print "tchau"
