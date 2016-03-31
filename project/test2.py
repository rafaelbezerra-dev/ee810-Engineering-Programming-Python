#! /usr/bin/python

import vlc
import pafy #https://github.com/mps-youtube/pafy
import time
import socket
import threading
import SocketServer

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    # def __init__(self, request, client_address, server):
    #     SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
    #     return

    def handle(self):

        data = self.request.recv(1024).strip()
        if " " not in data:
            data += " "
        print ">> {}".format(data)

        command, args = data.split(' ', 1)
        if command == "/play":
            if args:
                video = pafy.new(args)
                url = video.getbest().url
                self.server.player.set_media(instance.media_new(url))
            self.server.player.play()
        elif command == "/pause":
            self.server.player.pause()

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    def __init__(self, server_address, player, handler_class=ThreadedTCPRequestHandler):
        self.player = player
        SocketServer.TCPServer.__init__(self, server_address, handler_class)
        return


if __name__ == "__main__":
    instance = vlc.Instance('--no-fullscreen')
    # url = "https://www.youtube.com/watch?v=_V7ZKk-NJVA"
    url = "https://www.youtube.com/watch?v=OPf0YbXqDm0"
    video = pafy.new(url)
    movie = video.getbest().url
    player = instance.media_player_new()

    HOST, PORT = "localhost", 9996
    server = ThreadedTCPServer((HOST, PORT), player)
    ip, port = server.server_address
    print "Server running at:", ip, port
    # server.setPlayer(player)
    server_thread = threading.Thread(name="thr_server", target=server.serve_forever)
    server_thread.daemon = True
    # server_thread.allow_reuse_address = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name

    try:
        player.set_media(instance.media_new(movie))
        # player.play()
        # player.pause()
        while True:
            pass
    except KeyboardInterrupt:
        print "Server Interrupted"

    print "Shutting down"
    player.stop()
    server.shutdown()
    server.server_close()
    print "Bye"
