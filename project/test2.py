#! /usr/bin/python

import sys, time
import vlc, pafy #https://github.com/mps-youtube/pafy
import threading, socket, SocketServer

from Queue import Queue

class YouTubeVideo:
    pass

class YouTubePlayer:
    def __init__(self):
        self.instance = vlc.Instance('--no-fullscreen')
        self.player = self.instance.media_player_new()
        self.queue = Queue()
        self.is_playing = False
        self.is_media_set = False
    def play(self):
        if not self.is_playing:
            if not self.is_media_set:
                url = str(self.queue.get())
                video = pafy.new(url)
                url = video.getbest().url
                self.player.set_media(self.instance.media_new(url))
                self.queue.task_done()
                self.is_media_set = True
            self.player.play()
        return
    def pause(self):
        if self.is_playing:
            self.player.pause()
        return
    def stop(self):
        self.player.stop()
        return

    def next(self):
        url = str(self.queue.get())
        video = pafy.new(url)
        url = video.getbest().url
        self.player.set_media(self.instance.media_new(url))
        self.queue.task_done()
        self.is_media_set = True
        self.player.play()
        return

    def enqueue(self, url):
        self.queue.put(url)
        arr = [url for url in self.queue.queue]
        print "QUEUE:"
        index = 1
        for url in arr:
            print "  ", index, ": ", url
            index += 1
        return



class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):

        data = self.request.recv(1024).strip()
        if " " not in data:
            data += " "
        print ">> {}".format(data)

        command, args = data.split(' ', 1)
        if command == "/play":
            # if args:
            #     video = pafy.new(args)
            #     url = video.getbest().url
            #     self.server.player.set_media(instance.media_new(url))
            self.server.player.play()
        elif command == "/pause":
            self.server.player.pause()
        elif command == "/next":
            self.server.player.next()
        elif command == "/add":
            if args:
                self.server.player.enqueue(args)
        data = ""
        response = "{} {}".format(200, data)
        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    def __init__(self, server_address, player, handler_class=ThreadedTCPRequestHandler):
        self.player = player
        SocketServer.TCPServer.__init__(self, server_address, handler_class)
        return


if __name__ == "__main__":
    # instance = vlc.Instance('--no-fullscreen')
    # url = "https://www.youtube.com/watch?v=OPf0YbXqDm0"
    # video = pafy.new(url)
    # movie = video.getbest().url
    # player = instance.media_player_new()
    player = YouTubePlayer()

    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    # HOST, PORT = "localhost", 9995
    server = ThreadedTCPServer((HOST, PORT), player)
    ip, port = server.server_address
    print "Server running at:", ip, port
    server_thread = threading.Thread(name="thr_server", target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name

    try:
        # player.set_media(instance.media_new(movie))
        # player.play()
        # player.pause()
        while True:
            pass
    except KeyboardInterrupt:
        print "\nServer Interrupted"

    print "Shutting down"
    player.stop()
    server.shutdown()
    server.server_close()
    print "Bye"
