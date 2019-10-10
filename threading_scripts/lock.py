import threading
from urllib import request


class WorkerThread(threading.Thread):
    def __init__(self, url_list, url_list_lock):
        super(WorkerThread, self).__init__()
        self.url_list = url_list
        self.url_list_lock = url_list_lock

    def run(self):
        while True:
            next_url = self.grab_next_url()
            if next_url is None:
                break
            self.retrieve_url(next_url)

    def grab_next_url(self):
        with url_list_lock:
            if len(self.url_list) < 1:
                next_url = None
            else:
                next_url = self.url_list[0]
                del self.url_list[0]
            return next_url

    @staticmethod
    def retrieve_url(next_url):
        text = request.urlopen(next_url).read()
        print(f'{next_url}, {text}')


url_list = ['http://linux.org.ru', 'http://kernel.org', 'http://python.org']
url_list_lock = threading.Lock()

for x in range(0, 3):
    new_thread = WorkerThread(url_list, url_list_lock)
    new_thread.start()
