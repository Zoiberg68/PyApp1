import debugpy
#debugpy.listen(('192.168.1.8',5678))
#print('waiting...')
#debugpy.wait_for_client()


import pydevd_file_utils
import time, os
import random
from threading import Thread

class Thrd(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        amount = random.randint(1,3)
        time.sleep(amount)
        msg = '%s is running' % self.name
        print(msg)

def create_threads():
        for i in range(5):
            name = 'Thread #%s' % (i+1)
            my_thread = Thrd(name)
            #my_thread.start()

port='com4'
def getbyte():
    print('getbyte func')
    return 0


debugpy.log_to('/usr/src/PyApp1/PyApp1/')
getbyte()

print('start: '+ __name__)
print('file:'+ __file__)
print(pydevd_file_utils.__file__)

if __name__ == '__main__':
    create_threads()

print('THe end')




