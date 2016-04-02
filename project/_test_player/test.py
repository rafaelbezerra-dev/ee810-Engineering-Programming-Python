import sys
from omxplayer import OMXPlayer
from time import sleep


args = ['-vol -1500.00']
#player = OMXPlayer(sys.argv[1], args=['--no-osd', '--no-keys', '-b'])
player = OMXPlayer(sys.argv[1], args=args)
#player = OMXPlayer(sys.argv[1])


#player.set_volume(-1500.00)
player.play()
sleep(5)
player.pause()

player.quit()
