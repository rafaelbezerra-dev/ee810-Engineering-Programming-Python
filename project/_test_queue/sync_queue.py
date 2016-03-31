from Queue import Queue
import threading
import time

num_worker_threads = 5
q = Queue()

def worker():
    counter = 0
    cur_thread = threading.current_thread()
    name = cur_thread.name
    print "Starting", name
    while counter < 10:
        info = name + " counted to " + str(counter)
        q.put(info)
        counter += 1
        time.sleep(.1)

        # item = q.get()
        # do_work(item)
        # q.task_done()
    while True:
        pass

for i in range(num_worker_threads):
     t = threading.Thread(target=worker)
     t.daemon = True
     t.start()

while True:
    item = q.get()
    print item
    q.task_done()
    time.sleep(.5)

while True:
    pass
